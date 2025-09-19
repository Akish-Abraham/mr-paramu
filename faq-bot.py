import os
import json
from difflib import SequenceMatcher
from dotenv import load_dotenv
import google.generativeai as genai

# Load env variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=API_KEY)

# Load FAQ data
with open("faq.json", "r", encoding="utf-8") as f:
    faq_data = json.load(f)

# Find best matching FAQ
def find_best_match(user_input, cutoff=0.65):
    bestq, best_score = None, 0
    for q in faq_data.keys():
        score = SequenceMatcher(None, user_input.lower(), q.lower()).ratio()
        if score > best_score:
            bestq, best_score = q, score
    if best_score >= cutoff:
        return faq_data[bestq]
    else:
        return None

# Ask Gemini if no FAQ match
def ask_gemini(prompt):
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)
    return response.text

# CLI Loop
print("🤖 MR.Paramu – Ask me anything (type 'exit' to quit)\n")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("MR.Paramu: Goodbye 👋")
        break
    else:
        faq_answer = find_best_match(user_input)
        if faq_answer:
            print(f"MR.Paramu: {faq_answer}\n")
        else:
            ai_answer = ask_gemini(user_input)
            print(f"MR.Paramu : {ai_answer}\n")
