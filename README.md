# 🛡️ CyberJob Scout

**CyberJob Scout** is an offline, AI-flavored chatbot that helps students and job
seekers discover **Cyber Security internship** opportunities. It combines a
Python web scraper with a fully client-side chat interface, so once the data
is scraped, the chatbot works completely offline — no API calls, no server.

---

## ✨ Features

- 🔍 **Natural language search** — ask things like *"Jobs in Bengaluru"*,
  *"SOC roles"*, or *"What skills should I learn?"* and get relevant results
- 💬 **Chat-style UI** — typing indicators, message bubbles, and quick-reply chips
- 🏢 **Company & city filters** — automatically detects companies hiring and
  filters listings by Indian cities (Bengaluru, Mumbai, Hyderabad, Pune,
  Chennai, Noida, Delhi, Kolkata)
- 🧠 **Skill roadmap generator** — aggregates the most in-demand skills across
  all scraped listings so users know what to learn next
- 🕷️ **Automated scraper** — pulls fresh listings from LinkedIn and Indeed
  using Playwright, filtering out sponsored/promoted posts
- 📦 **Zero backend** — the chatbot is a single self-contained HTML file;
  data lives in a local JSON file

---

## 🗂️ Project Structure
jobscrape/
├── index.html              # Main chatbot UI (HTML + CSS + JS, self-contained)
├── jobscrap.py              # Playwright scraper (LinkedIn + Indeed)
├── job_listings.json        # Scraped job data consumed by the chatbot
├── README.md
├── LICENSE
├── .vscode/
│   └── launch.json          # VS Code launch config (opens index.html in Chrome)
└── src/                      # Reference copies of the chatbot's building blocks
├── style.css
├── chat_engine.js        # Message rendering, typing indicator, send/keyboard handling
├── ai_smart_search_engine.js   # Keyword search + intent-based reply builder
├── render_function.js
└── html_skeleton.html
---

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A modern browser (Chrome, Edge, Firefox)

### 1. Install dependencies
```bash
pip install playwright
playwright install chromium
```

### 2. Run the scraper
```bash
python jobscrap.py
```
This opens a visible Chromium window, searches LinkedIn and Indeed for
**"Cyber Security Internship"** roles in India posted in the last 24 hours,
skips promoted/sponsored posts, and writes up to 10 organic results per
platform into `job_listings.json`.

### 3. Open the chatbot
Just open `index.html` in your browser — no server required. The chat will
load listings from `job_listings.json` and respond to your questions about
them.

---

## ⚙️ How It Works

1. **Scraping (`jobscrap.py`)** — Uses Playwright to load LinkedIn and Indeed
   search result pages, extracts job title + link from each card, skips
   sponsored posts, and (currently) tags each listing with placeholder
   top skills via `ai_extract_skills()`.
2. **Search & Intent Engine (`src/ai_smart_search_engine.js`)** — Parses the
   user's message for intent (greeting, "show all", count, companies,
   skills roadmap, source filter, city filter) before falling back to a
   general keyword search across title, company, location, source, and
   skills.
3. **Chat Engine (`src/chat_engine.js`)** — Handles rendering messages,
   the animated typing delay, Enter-to-send, and highlighting the
   matching job card in the sidebar.

---

## 🛣️ Roadmap / Ideas

- [ ] Replace the placeholder `ai_extract_skills()` with real NLP-based
      skill extraction from job descriptions
- [ ] Add more cities and international locations
- [ ] Schedule the scraper to run automatically (cron / GitHub Actions)
- [ ] Add pagination for large result sets
- [ ] Persist chat history locally

---

## 🤝 Contributing

Issues and pull requests are welcome. If you spot a bug in the scraper
selectors (sites change their DOM often) or want to extend the chatbot's
intent detection, feel free to open a PR.

---

## 👤 Author

**Khushi Pancholi**
GitHub: [@Khushipancholi](https://github.com/Khushipancholi)

---
## 📄 License
MIT License
Copyright (c) 2026 Khushi Pancholi
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.





project is licensed under the **MIT License** — see below.
