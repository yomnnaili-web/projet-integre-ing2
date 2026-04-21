import os
import uuid
import logging
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify, make_response
from google import genai

load_dotenv()

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_key = os.getenv("GOOGLE_API_KEY")

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

    if not user_input:
        return jsonify({"reply": "Please enter a message."})

    try:
        if session_id not in chat_histories:
            chat_histories[session_id] = []

        chat_histories[session_id].append(f"User: {user_input}")
        context = "\n".join(chat_histories[session_id])

        response = client.models.generate_content(
            model=WORKING_MODEL,
            contents=context
        )

        reply = response.text

        chat_histories[session_id].append(f"AI: {reply}")

        return jsonify({"reply": reply})

    except Exception as e:
        logger.error(e)
        return jsonify({"reply": f"❌ Error: {str(e)}"})


if __name__ == "__main__":
    print("🚀 Running at http://127.0.0.1:5000")
    app.run(debug=True)