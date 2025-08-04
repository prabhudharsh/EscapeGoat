from flask import Flask, render_template, request, jsonify, stream_with_context, Response
import google.generativeai as genai
import json
import re

# Configure Gemini API
genai.configure(api_key="AIzaSyCGgXf5014M6H_vHsyJjPXypMZ3CMx9wRI")
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Chat history per session
chat_sessions = {}

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/next-field', methods=['POST'])
def next_field():
    data = request.get_json()
    session_id = data.get('session_id', 'default')
    fields = data.get('fields', {})

    if session_id not in chat_sessions:
        chat_sessions[session_id] = model.start_chat()
    chat = chat_sessions[session_id]

    # Rebuild context for EVERY call
    for label, answer in fields.items():
        chat.send_message(f"User answered: '{answer}' to the question: '{label}'")

    if len(fields) == 0:
        return jsonify({
            "label": "What are you trying to get away from using the excuse?",
            "type": "text"
        })

    if len(fields) >= 6:
        return jsonify({"ready": True})

    instruction = """
You are an interactive excuse-building AI.

🎯 GOAL:
Ask ONE next question to help build the most creative or believable excuse based on the user’s answers. 
Use CONTEXT FULLY. Do not repeat anything already asked or answered.
Use humor, logic, or absurdity only if it fits.

🎨 FORMAT:
Strict JSON ONLY:
- For dropdowns, use exactly 6 highly varied options (realistic to absurd)
- For sliders, use 1–10 scale (no 'options' field)
- For text, keep the label very clear

💡 RULES:
- Don’t ask about the same topic twice
- Cap total questions to 6 per user
- DO NOT include narrative or explanation
- DO NOT break JSON format
"""

    try:
        response = chat.send_message(instruction)
        content = response.text
        print("\n================ GEMINI RAW RESPONSE ================\n", content, "\n====================================================")

        match = re.search(r'\{.*\}', content, re.DOTALL)
        if not match:
            print("⚠️ Gemini returned NO PARSABLE JSON:", content)
            return jsonify({"label": "Oops! Invalid response from AI.", "type": "dropdown", "options": ["Retry"]})

        json_str = match.group()

        try:
            parsed = json.loads(json_str)
            print("✅ Parsed JSON:", parsed)
            return jsonify(parsed)
        except json.JSONDecodeError as je:
            print("❌ JSON Decode Error:", je)
            print("🔍 Problematic JSON string:", json_str)
            return jsonify({"label": "Oops! Couldn't understand the AI.", "type": "dropdown", "options": ["Retry"]})

    except Exception as e:
        print("🔥 Unhandled Error in /next-field:", str(e))
        return jsonify({"label": "Critical error occurred.", "type": "dropdown", "options": ["Retry"]})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    session_id = data.get('session_id', 'default')
    fields = data.get('fields', {})

    if session_id not in chat_sessions:
        chat_sessions[session_id] = model.start_chat()
    chat = chat_sessions[session_id]

    for label, answer in fields.items():
        chat.send_message(f"User answered: '{answer}' to the question: '{label}'")

    final_prompt = "Based on everything above, generate a smart, funny or absurd excuse. Be original. Only return the excuse as plain text."

    def stream_response():
        try:
            response = chat.send_message(final_prompt, stream=True)
            for chunk in response:
                if hasattr(chunk, 'text'):
                    yield chunk.text
        except Exception as e:
            print("🔥 Error during excuse generation:", str(e))
            yield f"❌ Error: {str(e)}"

    return Response(stream_with_context(stream_response()), content_type='text/plain')

if __name__ == '__main__':
    print("🚀 Starting Smart Excuse Generator with Gemini (context-persistent mode)...")
    app.run(debug=True)