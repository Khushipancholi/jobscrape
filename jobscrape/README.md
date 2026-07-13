# CyberJob Scout

An offline AI-flavored chatbot that helps job seekers browse Cyber Security internship
listings scraped from LinkedIn and Indeed.

## Structure

- `index.html` — the full chatbot UI (self-contained: HTML + CSS + JS in one file)
- `jobscrap.py` — Playwright scraper that pulls job listings from LinkedIn/Indeed into `job_listings.json`
- `job_listings.json` — scraped job data consumed by the chatbot
- `src/` — reference copies of the individual pieces the chatbot's inline `<script>`/`<style>` are built from:
  - `style.css`
  - `chat_engine.js` — message rendering, typing indicator, send/keyboard handling
  - `ai_smart_search_engine.js` — keyword search + intent-based reply builder
  - `render_function.js`
  - `html_skeleton.html`
- `.vscode/launch.json` — VS Code launch config for opening the chatbot in Chrome

## Running

1. Install deps: `pip install playwright && playwright install chromium`
2. Run the scraper: `python jobscrap.py` (produces `job_listings.json`)
3. Open `index.html` in a browser to chat with the scraped listings
