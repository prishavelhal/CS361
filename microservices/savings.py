from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Example data for two users, each with multiple goals
savings_goals = {
    "user123": [
        {"goal_name": "Vacation", "goal_amount": 1000, "current_amount": 400},
        {"goal_name": "Car", "goal_amount": 5000, "current_amount": 1500}
    ],
    "user456": [
        {"goal_name": "Emergency Fund", "goal_amount": 2000, "current_amount": 2000}
    ]
}

@app.route('/api/progress/<user_id>', methods=['GET'])
def get_progress(user_id):
    goals = savings_goals.get(user_id, [])
    for goal in goals:
        goal['progress'] = round((goal['current_amount'] / goal['goal_amount']) * 100, 2)
    return jsonify(goals)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)