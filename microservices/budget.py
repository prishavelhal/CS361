# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# budgets = {}

# @app.route('/budget', methods=['GET'])
# def get_budget():
#     print(f"getting budget: {budgets}")
#     return jsonify(budgets), 200

# @app.route('/budget', methods=['POST'])
# def add_budget():
#     data = request.json
#     print(f"POST request: {data}")
#     category = data.get("category")
#     amount = data.get("amount")

#     budgets[category] = amount
#     print(f"updated budget: {budgets}")
#     return jsonify({"message": "Budget successfully updated"}), 201

# if __name__ == '__main__':
#     app.run(debug=True, port=5003)