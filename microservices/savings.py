from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

# Example data for a user
savings_goals = {
    "goal_name": "Vacation", 
    "goal_amount": 1000, 
    "current_amount": 500,
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

if __name__ == '__main__':
    app.run(debug=True, port = 5005)