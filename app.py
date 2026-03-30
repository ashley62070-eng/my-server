from flask import Flask, request
import logging
import sqlite3

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# Create DB (if not exists)
def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return "Server Running"

@app.route('/api', methods=['POST'])
def receive():
    msg = request.form.get("message") or request.data.decode()

    # Save to DB
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("INSERT INTO messages (content) VALUES (?)", (msg,))
    conn.commit()
    conn.close()

    app.logger.info(f"🔥 Received: {msg}")

    return f"Stored: {msg}"

@app.route('/messages')
def get_messages():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM messages")
    rows = c.fetchall()
    conn.close()

    return str(rows)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
