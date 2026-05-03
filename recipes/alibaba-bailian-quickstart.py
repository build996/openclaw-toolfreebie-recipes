"""Alibaba Cloud Bailian quickstart — Qwen / DeepSeek / Coder via OpenAI SDK.

Bailian exposes Qwen Max, Qwen Plus, Qwen Coder, DeepSeek R1 and DeepSeek V3
behind an OpenAI-compatible endpoint, all on the free tier. This script shows
the bare minimum to call any of them.

Pairs with: https://toolfreebie.com/alibaba-bailian-free-api/

Setup:
  1. Get a key: https://bailian.console.aliyun.com/  → API-Key panel
  2. export BAILIAN_API_KEY=sk-...
  3. pip install openai
  4. python alibaba-bailian-quickstart.py
"""

import os
import sys
from openai import OpenAI

BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"

# Free-tier models worth knowing about. Quotas refresh per-model, not per-account.
MODELS = {
    "qwen-max":          "Frontier reasoning, ~1M tokens/month free",
    "qwen-plus":         "Strong middle-tier, generous quota",
    "qwen-coder-plus":   "Coding-specialized, recommended for IDE-style tasks",
    "deepseek-r1":       "R1 reasoning routed via Bailian",
    "deepseek-v3":       "V3 chat routed via Bailian",
}


def call(model: str, prompt: str) -> dict:
    client = OpenAI(api_key=os.environ["BAILIAN_API_KEY"], base_url=BASE_URL)
    resp = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )
    return {
        "model": resp.model,
        "answer": resp.choices[0].message.content,
        "tokens_in": resp.usage.prompt_tokens,
        "tokens_out": resp.usage.completion_tokens,
    }


def main():
    if "BAILIAN_API_KEY" not in os.environ:
        print("set BAILIAN_API_KEY first  (export BAILIAN_API_KEY=sk-...)", file=sys.stderr)
        sys.exit(1)

    prompt = "Explain prompt caching in three sentences a junior engineer would understand."

    for model in ["qwen-max", "deepseek-v3"]:
        print(f"\n=== {model} ===")
        try:
            r = call(model, prompt)
            print(r["answer"])
            print(f"\n[{r['tokens_in']} in / {r['tokens_out']} out]")
        except Exception as e:
            print(f"  failed: {e}")


if __name__ == "__main__":
    main()
