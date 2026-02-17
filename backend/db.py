import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="evote",
        password="1234",
        database="evote"
    )
