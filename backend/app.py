"""
BIS Sahayak API.

Runs two ways:

  python backend/app.py              -> stdlib http.server, zero installs
  uvicorn backend.app:api --reload   -> FastAPI, if you have it installed

Endpoints
  GET  /api/health
  GET  /api/config
  GET  /api/topics
  POST /api/ask     {"question": "...", "lang": "en"|"hi", "mode": "auto"|"groq"|"dataset", "api_key": "..."}
"""

import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from answer import (
    INDIC_LANGUAGES,
    compose,
    get_all_groq_keys,
    get_groq_model,
    is_groq_configured,
    translate_text,
)  # noqa: E402
from retriever import Retriever  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND = os.path.join(ROOT, "frontend")

RETRIEVER = Retriever()
DEVANAGARI = re.compile(r"[\u0900-\u097F]")


def detect_lang(text, declared=None):
    if declared in ("en", "hi"):
        return declared
    return "hi" if DEVANAGARI.search(text or "") else "en"


def handle_ask(payload, header_api_key=None):
    question = (payload.get("question") or "").strip()
    image_data = payload.get("image_data")
    image_name = payload.get("image_name")
    identified_item = (payload.get("identified_item") or "").strip()
    visual_predictions = payload.get("visual_predictions") or []

    # Prioritize actual visual content analysis over file names
    if not question and identified_item:
        question = f"What Indian Standard and BIS certification applies to {identified_item}? What is the IS number, definition, and for which things is it given to?"
    elif not question and visual_predictions:
        items_str = ", ".join(str(p) for p in visual_predictions[:2])
        question = f"An image was visually classified by computer vision as containing: {items_str}. What Indian Standard (IS) and BIS certification applies to this product?"
    elif not question and image_data:
        question = "What Indian Standard and BIS certification applies to this product? What is the IS number, definition, and for which things is it given to?"

    if not question:
        return {"error": "Type a question or select an item first."}, 400

    lang = detect_lang(question, payload.get("lang"))
    mode = payload.get("mode", "auto")
    api_key = payload.get("api_key") or header_api_key

    hits = RETRIEVER.search(question, top_k=3)
    result = compose(
        question=question,
        hits=hits,
        lang=lang,
        mode=mode,
        api_key=api_key,
    )
    result["lang"] = lang
    result["question"] = question
    if image_data:
        result["image_data"] = image_data
    if image_name:
        result["image_name"] = image_name
    if identified_item:
        result["identified_item"] = identified_item

    return result, 200


def handle_translate(payload, header_api_key=None):
    text = (payload.get("text") or "").strip()
    target_lang = (payload.get("target_lang") or "hi").strip()
    standard_card = payload.get("standard_card")
    api_key = payload.get("api_key") or header_api_key

    if not text:
        return {"error": "Missing text to translate"}, 400

    trans_text, trans_card = translate_text(
        text=text,
        target_lang=target_lang,
        api_key=api_key,
        standard_card=standard_card,
    )

    lang_info = INDIC_LANGUAGES.get(target_lang.lower(), ("Regional Language", target_lang))

    return {
        "translated_text": trans_text,
        "target_lang": target_lang,
        "lang_name": lang_info[0],
        "native_name": lang_info[1],
        "standard_card": trans_card,
    }, 200


def handle_topics():
    counts = {}
    for e in RETRIEVER.entries:
        counts[e["topic"]] = counts.get(e["topic"], 0) + 1
    unverified = sum(1 for e in RETRIEVER.entries if not e.get("verified"))
    return {
        "entries": len(RETRIEVER.entries),
        "by_topic": counts,
        "unverified": unverified,
    }, 200


def handle_config(header_api_key=None):
    server_keys = get_all_groq_keys()
    all_keys = get_all_groq_keys(header_api_key)
    server_configured = len(server_keys) > 0
    client_or_server_configured = len(all_keys) > 0
    return {
        "groq_configured": client_or_server_configured,
        "server_has_key": server_configured,
        "keys_count": len(all_keys),
        "server_keys_count": len(server_keys),
        "model": get_groq_model(),
        "entries": len(RETRIEVER.entries),
        "default_mode": "auto",
        "supported_languages": [
            {"code": "en", "name": "English", "native": "English"},
            {"code": "hi", "name": "Hindi", "native": "हिन्दी"},
            {"code": "ta", "name": "Tamil", "native": "தமிழ்"},
            {"code": "te", "name": "Telugu", "native": "తెలుగు"},
            {"code": "bn", "name": "Bengali", "native": "বাংলা"},
            {"code": "mr", "name": "Marathi", "native": "मराठी"},
        ],
    }, 200


# --- stdlib server -----------------------------------------------------------

class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        sys.stderr.write("%s %s\n" % (self.address_string(), fmt % args))

    def _send(self, obj, status=200):
        body = json.dumps(obj, ensure_ascii=False).encode("utf-8")
        try:
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Groq-Api-Key, X-Grok-Api-Key, Authorization")
            self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            pass

    def _send_file(self, path, ctype):
        with open(path, "rb") as f:
            body = f.read()
        try:
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
        except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):
            pass

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Groq-Api-Key, X-Grok-Api-Key, Authorization")
        self.send_header("Access-Control-Allow-Methods", "POST, GET, OPTIONS")
        self.end_headers()

    def do_GET(self):
        path = urlparse(self.path).path
        header_key = self.headers.get("X-Groq-Api-Key") or self.headers.get("X-Grok-Api-Key")
        if path == "/api/health":
            all_keys = get_all_groq_keys(header_key)
            return self._send({
                "status": "ok",
                "entries": len(RETRIEVER.entries),
                "groq_active": len(all_keys) > 0,
                "groq_keys_count": len(all_keys),
                "model": get_groq_model(),
            })
        if path == "/api/config":
            obj, code = handle_config(header_key)
            return self._send(obj, code)
        if path == "/api/topics":
            obj, code = handle_topics()
            return self._send(obj, code)
        if path in ("/", "/index.html"):
            return self._send_file(os.path.join(FRONTEND, "index.html"), "text/html; charset=utf-8")
        self._send({"error": "not found"}, 404)

    def do_POST(self):
        req_path = urlparse(self.path).path
        if req_path not in ("/api/ask", "/api/translate"):
            return self._send({"error": "not found"}, 404)
        length = int(self.headers.get("Content-Length") or 0)
        try:
            raw_body = self.rfile.read(length).decode("utf-8")
            payload = json.loads(raw_body or "{}")
        except Exception:
            return self._send({"error": "bad json"}, 400)

        header_key = self.headers.get("X-Groq-Api-Key") or self.headers.get("X-Grok-Api-Key")
        if req_path == "/api/translate":
            obj, code = handle_translate(payload, header_api_key=header_key)
        else:
            obj, code = handle_ask(payload, header_api_key=header_key)
        self._send(obj, code)


# --- optional FastAPI app ----------------------------------------------------

try:
    from fastapi import FastAPI, Header
    from fastapi.middleware.cors import CORSMiddleware
    from fastapi.responses import FileResponse
    from pydantic import BaseModel

    class Ask(BaseModel):
        question: str
        lang: str | None = None
        mode: str = "auto"
        api_key: str | None = None

    api = FastAPI(title="BIS Sahayak")
    api.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    )

    @api.get("/api/health")
    def health(x_groq_api_key: str | None = Header(default=None)):
        all_keys = get_all_groq_keys(x_groq_api_key)
        return {
            "status": "ok",
            "entries": len(RETRIEVER.entries),
            "groq_active": len(all_keys) > 0,
            "groq_keys_count": len(all_keys),
            "model": get_groq_model(),
        }

    @api.get("/api/config")
    def config(x_groq_api_key: str | None = Header(default=None)):
        return handle_config(x_groq_api_key)[0]

    @api.get("/api/topics")
    def topics():
        return handle_topics()[0]

    @api.post("/api/ask")
    def ask(body: Ask, x_groq_api_key: str | None = Header(default=None)):
        return handle_ask(body.model_dump(), header_api_key=x_groq_api_key)[0]

    @api.post("/api/translate")
    def translate(body: dict, x_groq_api_key: str | None = Header(default=None)):
        return handle_translate(body, header_api_key=x_groq_api_key)[0]

    @api.get("/")
    def index():
        return FileResponse(os.path.join(FRONTEND, "index.html"))

except ImportError:
    api = None


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    keys = get_all_groq_keys()
    print(f"BIS Sahayak running on http://localhost:{port}")
    print(f"Knowledge base: {len(RETRIEVER.entries)} entries")
    print(f"Groq API pool configured: {'Yes (' + str(len(keys)) + ' key(s) armed, ' + get_groq_model() + ')' if keys else 'No (Local dataset fallback mode active)'}")
    server = ThreadingHTTPServer(("0.0.0.0", port), Handler)
    server.daemon_threads = True
    server.serve_forever()
