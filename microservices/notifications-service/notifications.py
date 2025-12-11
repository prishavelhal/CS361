from flask import Flask, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
CORS(app)

reminders = [
    "Utilities bill due in 2 days",
    "Rent payment due in 5 days",
    "Pay credit card bill in 3 days",
    "Autopayment for insurance in 1 day",
    "Subscription service payment due in 7 days"
]

@app.route('/notifications', methods=['GET'])
def get_notification():
    reminder = random.choice(reminders)
    return jsonify({'notification': reminder})

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "running", "service": "notifications"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=False)