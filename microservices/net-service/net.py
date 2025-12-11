from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route('/net', methods=['POST'])
def calculate_net():
    data = request.json
    income = data.get('income', 0)
    expenses = data.get('expenses', 0)
    net = income - expenses
    return jsonify({'net': net})

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "running", "service": "net-balance"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5004))
    app.run(host='0.0.0.0', port=port, debug=False)