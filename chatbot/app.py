import os
import google.generativeai as genai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templatestrad', static_folder='static')

# --- CONFIGURATION ---
# Paste your REAL key from https://aistudio.google.com/ here
apiKey = "AIzaSyBIgdcFL2dHiH7wHqmXRCA5nM939DLrG-c" 
genai.configure(api_key=apiKey)

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction="You are a Career Expert. Only answer questions about studies and jobs."
)

chat_sessions = {}

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/message", methods=["POST"])
def message():
    user_id = request.remote_addr
    user_input = request.json.get("message")

    if user_id not in chat_sessions:
        chat_sessions[user_id] = model.start_chat(history=[])

    try:
        chat = chat_sessions[user_id]
        response = chat.send_message(user_input)
        return jsonify({"reply": response.text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "I'm having trouble with the API key or connection."}), 500

if __name__ == "__main__":
    print("--- SERVER STARTING ---")
    print("Go to http://127.0.0.1:5001")
    app.run(debug=True, port=5001)