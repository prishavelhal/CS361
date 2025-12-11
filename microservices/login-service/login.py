from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Test user
user = {
    "id": "test-user",
    "username": "user123",
    "password": "password123"
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username == user["username"] and password == user["password"]:
        return jsonify({"message": "Login Successful!", "user_id": user["id"]}), 200
    else:
        return jsonify({"message": "Error."}), 401

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "running", "service": "login"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port, debug=False)