"""Mistral AI quickstart — Nemo / Mistral-7B / Mixtral via OpenAI SDK.

Mistral's free tier exposes their open-source models behind an
OpenAI-compatible endpoint. The same code that calls GPT-4 calls Mistral —
just swap the base_url and model name.

Pairs with: https://toolfreebie.com/mistral-free-api/

Setup:
  1. Get a key: https://console.mistral.ai/api-keys
  2. export MISTRAL_API_KEY=...
  3. pip install openai
  4. python mistral-quickstart.py
"""

import os
import sys
from openai import OpenAI

BASE_URL = "https://api.mistral.ai/v1"

# Open-weight models on the free tier (closed-weight ones are paid):
FREE_MODELS = {
    "open-mistral-nemo":       "Nemo 12B — best speed/quality tradeoff on free tier",
    "open-mistral-7b":         "Original Mistral 7B",
    "open-mixtral-8x7b":       "MoE, slower but higher ceiling",
    "open-mixtral-8x22b":      "Larger MoE, may be intermittently rate-limited",
}


def call(model: str, prompt: str, system: str | None = None) -> str:
    client = OpenAI(api_key=os.environ["MISTRAL_API_KEY"], base_url=BASE_URL)
    messages = []
    if system:
        messages.append({"role": "system", "content": system})
    messages.append({"role": "user", "content": prompt})
    r = client.chat.completions.create(
        model=model,
        messages=messages,
        max_tokens=400,
        temperature=0.7,
    )
    return r.choices[0].message.content


def main():
    if "MISTRAL_API_KEY" not in os.environ:
        print("set MISTRAL_API_KEY first", file=sys.stderr)
        sys.exit(1)

    for model in ["open-mistral-nemo", "open-mixtral-8x7b"]:
        print(f"\n=== {model} ===")
        try:
            answer = call(
                model,
                "List three well-known things about Brittany (the region in France).",
                system="You are concise. No preamble. Use bullet points.",
            )
            print(answer)
        except Exception as e:
            print(f"  failed: {e}")


if __name__ == "__main__":
    main()
