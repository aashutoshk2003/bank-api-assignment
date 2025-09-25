from flask import Flask, jsonify
import json

app = Flask(__name__)  # Create Flask app

# Load bank data from JSON file
with open('banks.json') as f:
    banks_data = json.load(f)

# Route 1: Get all banks
@app.route('/banks', methods=['GET'])
def get_banks():
    banks_list = [{"bank_id": bank["bank_id"], "name": bank["name"]} for bank in banks_data]
    return jsonify(banks_list)

# Route 2: Get branch details by branch_id
@app.route('/branches/<int:branch_id>', methods=['GET'])
def get_branch(branch_id):
    for bank in banks_data:
        for branch in bank["branches"]:
            if branch["branch_id"] == branch_id:
                branch_info = {
                    "branch": branch["branch"],
                    "ifsc": branch["ifsc"],
                    "bank": {"bank_id": bank["bank_id"], "name": bank["name"]}
                }
                return jsonify(branch_info)
    return jsonify({"error": "Branch not found"}), 404

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
