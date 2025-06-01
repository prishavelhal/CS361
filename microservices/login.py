from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# create test users
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
        return jsonify({"message": " Error."}), 401

if __name__ == '__main__':
    app.run(debug=True, port=5002)