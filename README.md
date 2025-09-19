# MR.Paramu – CLI FAQ Bot 🤖

MR.Paramu is a **Command Line Interface (CLI) FAQ bot** created by **Akish Babu Abraham**.  
It answers questions from a local FAQ file, and if no good match is found, it falls back to **Gemini AI**.

---

## ✨ Features
- Hardcoded FAQ responses (from `faq.json`)
- Fuzzy matching (handles typos and similar phrasing)
- AI fallback using Gemini
- CLI-based interaction

---

## 🚀 Getting Started

### 1. Clone this repo
```bash
git clone https://github.com/Akish-Abraham/faq-bot.git
cd faq-bot

2. Install dependencies
pip install -r requirements.txt

3. Set up environment variables

Option A: System environment variable

Add GEMINI_API_KEY to your system variables (recommended).

Option B: .env file (local use)

Copy .env.example to .env and add your Gemini API key:
GEMINI_API_KEY=your_api_key_here

4. Run the bot
python faqbot.py

Example Usage

🤖 MR.Paramu – Ask anything (type 'exit' to quit)

You: What is your refund policy?
Bot: Refunds are available within 7 days of purchase.

You: Who created you?
Bot: I was created by Akish Babu Abraham 👨‍💻.

You: Tell me a joke
Bot (AI): Why don’t programmers like nature? Too many bugs 🐞😂

👨‍💻 Creator

Built with ❤️ by Akish Babu Abraham.
Bot name: MR.Paramu 🤖

📜 License

This project is licensed under the MIT License.