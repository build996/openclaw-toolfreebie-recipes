# Render Free Tier — Hello World Deploy

A minimal Flask app + `render.yaml` Blueprint that deploys to [Render](https://render.com)'s free Web Service tier in one click.

Pairs with the long-form review: [Render Free Hosting Review 2026](https://toolfreebie.com/render-hosting-review/)

## What you get

- 1 Render free Web Service running `app.py`
- Auto-deploys on every push to `main`
- Sleeps after 15 min of inactivity (free tier behavior)
- ~30s cold start when sleeping

## Deploy

1. Push these files to a GitHub repo of your own (or fork this one).
2. Open https://dashboard.render.com/ → **New** → **Blueprint**.
3. Connect the repo. Render reads `render.yaml` and proposes the service.
4. Click **Apply**. First build takes ~2 minutes.
5. Hit the auto-generated `https://<name>.onrender.com/` URL — you should see "Hello from Render free tier!".

## Files

- `app.py` — Flask app, single route, port from `$PORT` (Render injects).
- `render.yaml` — Blueprint config: Python runtime, free plan, no DB.
- `requirements.txt` — `flask` only.

## What's NOT free here

- Persistent disks (the free Web Service has no writable disk between deploys).
- Background workers (free tier is web-only).
- Custom domains require manual TLS setup but are free.

For the full breakdown of what Render's free tier covers, see the [review article](https://toolfreebie.com/render-hosting-review/).
