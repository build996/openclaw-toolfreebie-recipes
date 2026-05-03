"""DeepSeek API quickstart — R1 reasoning + V3 chat in 30 lines.

Two models matter on DeepSeek's free tier:
  - deepseek-chat       (V3, fast general chat)
  - deepseek-reasoner   (R1, exposes the <think> trace via reasoning_content)

This script calls each once so you can see the difference between them.

Pairs with: https://toolfreebie.com/deepseek-free-api/

Setup:
  1. Get a key: https://platform.deepseek.com/api_keys
  2. export DEEPSEEK_API_KEY=sk-...
  3. pip install openai
  4. python deepseek-quickstart.py
"""

import os
import sys
from openai import OpenAI


def client() -> OpenAI:
    return OpenAI(api_key=os.environ["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")


def chat_v3(prompt: str) -> str:
    """Fast general-purpose chat — use this for 90% of requests."""
    r = client().chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=400,
    )
    return r.choices[0].message.content


def reason_r1(prompt: str) -> dict:
    """R1 reasoning — returns both the reasoning trace and the final answer.

    The reasoning is exposed in `message.reasoning_content`, separate from the
    user-facing `message.content`. You can log/store the trace without leaking
    it to end users.
    """
    r = client().chat.completions.create(
        model="deepseek-reasoner",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=2000,
    )
    msg = r.choices[0].message
    return {
        "reasoning": getattr(msg, "reasoning_content", "") or "",
        "answer": msg.content,
    }


def main():
    if "DEEPSEEK_API_KEY" not in os.environ:
        print("set DEEPSEEK_API_KEY first", file=sys.stderr)
        sys.exit(1)

    print("=== V3 chat (deepseek-chat) ===")
    print(chat_v3("What is the capital of France? Answer in one word."))

    print("\n=== R1 reasoning (deepseek-reasoner) ===")
    out = reason_r1(
        "A train leaves NYC at 3pm going 60mph toward Chicago. Another leaves "
        "Chicago at 4pm going 80mph toward NYC. NYC-Chicago is 800 miles. "
        "When and where do they meet?"
    )
    print("Reasoning trace (first 400 chars):")
    print(out["reasoning"][:400] + ("..." if len(out["reasoning"]) > 400 else ""))
    print("\nFinal answer:")
    print(out["answer"])


if __name__ == "__main__":
    main()
