from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Example savings data
savings_goals = {
    "goal_name": "Vacation", 
    "goal_amount": 1000, 
    "current_amount": 573,
}

@app.route('/progress', methods=['GET'])
def get_progress():
    progress = round((savings_goals["current_amount"] / savings_goals["goal_amount"]) * 100, 2)
    return jsonify({
        "goal_name": savings_goals["goal_name"],
        "goal_amount": savings_goals["goal_amount"],
        "current_amount": savings_goals["current_amount"],
        "progress": progress
    })

@app.route('/', methods=['GET'])
def health():
    return jsonify({"status": "running", "service": "savings-progress"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5005))
    app.run(host='0.0.0.0', port=port, debug=False)