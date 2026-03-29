from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server Running"

@app.route('/api', methods=['POST'])
def receive():
    msg = request.form.get("message")

    # fallback if form is empty
    if not msg:
        msg = request.data.decode()

    print("Received:", msg)

    return f"Received: {msg}"

app.run(host="0.0.0.0", port=10000)
