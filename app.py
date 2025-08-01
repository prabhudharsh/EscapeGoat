from flask import Flask, render_template, request, Response
import subprocess

app = Flask(__name__)

def generate_stream(prompt):
    # Launch Ollama with streaming
    process = subprocess.Popen(
        ["ollama", "run", "llama3:8b"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1
    )

    # Send the prompt
    process.stdin.write(prompt)
    process.stdin.close()

    # Yield output line-by-line
    for line in process.stdout:
        yield f"data: {line.strip()}\n\n"

    process.stdout.close()
    process.wait()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/stream")
def stream():
    data = request.args
    prompt = f"""
You are an excuse generator. Generate an excuse based on the parameters below. Output only the excuse. No explanation.

Creativity Level Guide:
- 1 = Realistic
- 5 = Mildly creative
- 7 = Bizarre
- 10 = Pure chaos, make it unhinged, break reality

🧾 Context: {data['situation']}
🔧 Severity Level: {data['severity']}
🎭 Style: {data['style']}
🎯 Blame Target: {data['blame']}
🗣️ Length: {data['length']}
👔 Profession: {data['profession']}
🕒 Time of Day: {data['time']}
🌈 Creativity Level: {data['creativity']}

Now generate the excuse.
"""
    return Response(generate_stream(prompt), mimetype='text/event-stream')
