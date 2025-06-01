from flask import Flask, jsonify
from flask_cors import CORS
import random

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

if __name__ == '__main__':
    app.run(debug=True, port=5001)