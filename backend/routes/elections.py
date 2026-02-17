from flask import Blueprint, request, jsonify
from datetime import date
from db import get_connection

elections_bp = Blueprint("elections", __name__)

@elections_bp.route("/elections", methods=["GET"])
def get_elections():
    status = request.args.get("status")
    name = request.args.get("name")
    date_filter = request.args.get("date")

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM elections WHERE 1=1"
    params = []
    today = date.today()

    if status == "upcoming":
        query += " AND start_date > %s"
        params.append(today)
    elif status == "active":
        query += " AND start_date <= %s AND end_date >= %s"
        params.extend([today, today])
    elif status == "closed":
        query += " AND end_date < %s"
        params.append(today)

    if name:
        query += " AND name LIKE %s"
        params.append(f"%{name}%")

    if date_filter:
        query += " AND start_date = %s"
        params.append(date_filter)

    cursor.execute(query, params)
    return jsonify(cursor.fetchall())
