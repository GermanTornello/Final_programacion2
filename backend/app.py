from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection
from routes.elections import elections_bp

app = Flask(__name__)
CORS(app)
app.register_blueprint(elections_bp)

@app.route("/ping")
def ping():
    return "PONG"

@app.route("/")
def home():
    return "eVote System API"

@app.route("/test-db")
def test_db():
    conn = get_connection()
    return "DB OK"

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data["email"]
    password = data["password"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, name, role FROM users WHERE email=%s AND password=%s",
        (email, password)
    )
    user = cursor.fetchone()

    if not user:
        return jsonify({"error": "Credenciales inválidas"}), 401

    return jsonify(user)

if __name__ == "__main__":
    app.run(debug=True)
