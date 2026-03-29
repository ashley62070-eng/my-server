from flask import Flask, request
import logging

app = Flask(__name__)

# Enable proper logging (important for Render)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return "Server Running"

@app.route('/api', methods=['POST'])
def receive():
    # Get message from form or raw body
    msg = request.form.get("message") or request.data.decode()

    # Log it (this WILL show in Render logs)
    app.logger.info(f"🔥 Received: {msg}")

    # Return response
    return f"Received: {msg}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
