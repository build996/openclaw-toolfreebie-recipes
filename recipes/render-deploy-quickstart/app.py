"""Minimal Flask app for Render's free Web Service tier.

Pairs with: https://toolfreebie.com/render-hosting-review/

Render injects the PORT env var. Bind to 0.0.0.0 — localhost won't reach the
public listener.
"""
import os
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello from Render free tier!\n"


@app.route("/health")
def health():
    return jsonify(status="ok")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
