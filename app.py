from flask import Flask, request

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def receive():
    msg = request.form.get("message")

    print("Received:", msg)

    with open("data.txt", "a") as f:
        f.write(msg + "\n")

    return "OK"

@app.route('/')
def home():
    return "Server Running"

app.run(host="0.0.0.0", port=10000)
