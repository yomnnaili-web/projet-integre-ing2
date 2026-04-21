import os
import uuid
import logging
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, make_response
from google import genai

env_path = Path(__file__).resolve().parent / ".env"
print("Looking for .env at:", env_path)
print("Exists:", env_path.exists())

load_dotenv(env_path)

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_key = os.getenv("GOOGLE_API_KEY", "").strip()
print("Key loaded:", bool(api_key))
print("Key preview:", api_key[:10] if api_key else "None")

if not api_key:
    print("❌ No API key found in .env")
    exit(1)

# Init client
client = genai.Client(api_key=api_key)

# 🔍 Detect working model automatically
print("🔍 Detecting available models...")

WORKING_MODEL = None

try:
    models = client.models.list()

    for m in models:
        print("Found model:", m.name)

        # pick first usable Gemini model
        if "gemini" in m.name.lower():
            WORKING_MODEL = m.name
            break

    if not WORKING_MODEL:
        print("❌ No Gemini models available for this API key")
        exit(1)

    print(f"✅ Using model: {WORKING_MODEL}")

except Exception as e:
    print("❌ Cannot list models:", e)
    exit(1)


chat_histories = {}

def get_session_id(req):
    return req.cookies.get("session_id") or str(uuid.uuid4())

@app.route("/")
def home():
    resp = make_response(render_template("chat.html"))
    session_id = str(uuid.uuid4())
    resp.set_cookie("session_id", session_id, max_age=7*24*60*60)
    chat_histories[session_id] = []
    return resp



@app.route("/message", methods=["POST"])
def message():
    user_input = request.json.get("message", "").strip()
    session_id = get_session_id(request)

    print("=== /message hit ===")
    print("User input:", user_input)
    print("Key preview:", api_key[:10] if api_key else "None")
    print("Model:", WORKING_MODEL)

    if not user_input:
        return jsonify({"reply": "Please enter a message."}), 400

    try:
        response = client.models.generate_content(
            model=WORKING_MODEL,
            contents=user_input
        )

        reply = response.text or "No response text returned."
        return jsonify({"reply": reply}), 200

    except Exception as e:
        logger.exception("Route error")
        return jsonify({"reply": f"❌ Error: {str(e)}"}), 500
    
if __name__ == "__main__":
    print("🚀 Running at http://127.0.0.1:5000")
    app.run(debug=False, use_reloader=False)