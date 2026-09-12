"""
Vercel Serverless Function entrypoint for BIS Sahayak.
"""
import os
import sys

# Ensure backend and root paths are available for imports
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(CURRENT_DIR)
BACKEND_DIR = os.path.join(ROOT_DIR, "backend")

for p in (BACKEND_DIR, ROOT_DIR):
    if p not in sys.path:
        sys.path.insert(0, p)

from app import Handler

class handler(Handler):
    """
    Vercel invokes subclasses of BaseHTTPRequestHandler named 'handler'
    in Python Serverless Functions.
    """
    pass
