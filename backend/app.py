from flask import Flask, request, jsonify, session
from flask_cors import CORS
from routes.elections import elections_bp
from db import get_connection

app = Flask(__name__)

# ---------------- CONFIG ----------------

app.secret_key = "supersecretkey"

app.config["SESSION_COOKIE_SAMESITE"] = "Lax"
app.config["SESSION_COOKIE_SECURE"] = False

# CORS (IMPORTANTE)
CORS(app,
     supports_credentials=True,
     origins=["http://localhost:8000"]
)






# ---------------- BLUEPRINTS ----------------

app.register_blueprint(elections_bp)

# ---------------- TEST ----------------

@app.route("/ping")
def ping():
    return "PONG"

@app.route("/")
def home():
    return "eVote System API"

@app.route("/test-db")
def test_db():
    conn = get_connection()
    conn.close()
    return "DB OK"

# ---------------- LOGIN ----------------
# ---------------- LOGIN ----------------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No llegaron datos"}), 400

    email = data.get("email")
    password = data.get("password")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 401

    if user["password"] != password:
        return jsonify({"error": "Contraseña incorrecta"}), 401

    # Guardar sesión
    session["user_id"] = user["id"]
    session["role"] = user["role"]
    print("ROLE GUARDADO:", session["role"])


    return jsonify({
        "message": "Login correcto",
        "email": user["email"]
    })



# ---------------- CANDIDATOS ----------------

@app.route("/candidates/<int:election_id>", methods=["GET"])
def get_candidates(election_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name FROM candidates WHERE election_id=%s",
        (election_id,)
    )

    candidates = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(candidates)


# ---------------- VOTAR ----------------

@app.route("/vote", methods=["POST"])
def vote():

    if "user_id" not in session:
        return jsonify({"error": "No autenticado"}), 401

    if session["role"] != "votar":
        return jsonify({"error": "No autorizado"}), 403

    data = request.get_json(force=True)

    election_id = data["election_id"]
    candidate_id = data["candidate_id"]

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        "SELECT status FROM elections WHERE id=%s",
        (election_id,)
    )

    election = cursor.fetchone()

    if not election or election["status"] != "active":
        cursor.close()
        conn.close()
        return jsonify({"error": "La elección no está activa"}), 400

    try:
        cursor.execute("""
            INSERT INTO votes (user_id, election_id, candidate_id, timestamp)
            VALUES (%s, %s, %s, NOW())
        """, (session["user_id"], election_id, candidate_id))

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({"message": "Voto registrado correctamente"})

    except Exception as e:
        print("ERROR VOTO:", str(e))
        cursor.close()
        conn.close()
        return jsonify({"error": "Ya votaste en esta elección"}), 400


@app.route("/results/<int:election_id>", methods=["GET"])
def results(election_id):

    # 🔒 Solo admin
    if "user_id" not in session:
        return jsonify({"error": "No autenticado"}), 401

    if session.get("role") != "admin":
        return jsonify({"error": "No autorizado"}), 403

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # votos por candidato
    cursor.execute("""
        SELECT c.name, COUNT(v.id) as votes
        FROM candidates c
        LEFT JOIN votes v ON c.id = v.candidate_id
        WHERE c.election_id = %s
        GROUP BY c.id
        ORDER BY votes DESC
    """, (election_id,))

    results = cursor.fetchall()

    # total votos
    total_votes = sum(r["votes"] for r in results)

    # agregar porcentaje
    for r in results:
        if total_votes > 0:
            r["percentage"] = round((r["votes"] / total_votes) * 100, 2)
        else:
            r["percentage"] = 0

    cursor.close()
    conn.close()

    return jsonify({
        "total_votes": total_votes,
        "results": results
    })

# ---------------- LOGOUT ----------------

@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"message": "Sesión cerrada"})


# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)

