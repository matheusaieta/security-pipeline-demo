from flask import Flask, request
import sqlite3

app = Flask(__name__)

# FAKE SECRET: This will trigger the Secret Detector
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

@app.route("/login")
def login():
    # INSECURE CODE: This will trigger the SAST Code Scanner (SQL Injection)
    username = request.args.get('user')
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute(query)
    return "Logged In"
