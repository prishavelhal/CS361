from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/net', methods=['POST'])
def calculate_net():
    data = request.json
    income = data.get('income', 0)
    expenses = data.get('expenses', 0)
    net = income - expenses
    return jsonify({'net': net})


if __name__ == '__main__':
    app.run(debug=True, port=5004)