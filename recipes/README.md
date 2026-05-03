# Recipes

Each file here is a minimal, runnable example for one of the tools reviewed at [toolfreebie.com](https://toolfreebie.com). The header comment in every file links back to the matching long-form review.

## What's in here

| File | Pairs with article | What it does |
|---|---|---|
| [`alibaba-bailian-quickstart.py`](./alibaba-bailian-quickstart.py) | [Alibaba Cloud Bailian API](https://toolfreebie.com/alibaba-bailian-free-api/) | Calls Qwen Max + DeepSeek V3 through Bailian's OpenAI-compatible endpoint |
| [`deepseek-quickstart.py`](./deepseek-quickstart.py) | [DeepSeek API](https://toolfreebie.com/deepseek-free-api/) | Calls V3 chat + R1 reasoning, shows how to read R1's `reasoning_content` trace |
| [`mistral-quickstart.py`](./mistral-quickstart.py) | [Mistral AI Free API](https://toolfreebie.com/mistral-free-api/) | Calls Nemo + Mixtral via OpenAI SDK against `api.mistral.ai/v1` |
| [`render-deploy-quickstart/`](./render-deploy-quickstart/) | [Render Free Hosting Review](https://toolfreebie.com/render-hosting-review/) | Flask hello-world + `render.yaml` Blueprint for Render's free Web Service tier |

## Format

- `*.py` — Python quickstarts. Run with `python <file>` after the env-var setup
  in each file's docstring.
- Subfolders (e.g. `render-deploy-quickstart/`) — multi-file recipes (have their
  own README).
- More tool-specific OpenClaw task JSONs land here as the corresponding articles
  are written or revisited.

## Why nothing for Google NotebookLM?

NotebookLM has no public API as of 2026-05. The [review article](https://toolfreebie.com/notebooklm-ai-research/) covers the manual workflow; no automation recipe is possible until Google ships one.
