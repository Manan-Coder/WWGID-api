from flask import Flask, jsonify, request, render_template
from datetime import datetime
import random
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

DATA_FILE = "entries.json"

def load_entries():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_entries():
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=4)

entries = load_entries()

@app.route("/home")
def main():
    return render_template("index.html")

@app.route("/api/add", methods=['POST'])
def add():
    data = request.get_json()
    if not data or not data.get("entry"):
        return jsonify({"error": "No entry provided"}), 400
    
    new_entry = {
        'id': len(entries) + 1,
        'entry': data["entry"],
        'date': datetime.now().strftime("%Y-%m-%d")
    }
    entries.append(new_entry)
    save_entries()
    return jsonify({'message': 'Entry added successfully', 'id': new_entry['id']})

@app.route("/api/get-all", methods=['GET'])
def get_entries():
    if not entries:
        return jsonify({"error": "No entries found"}), 404
    return jsonify(entries)

@app.route("/api/get-random", methods=['GET'])
def get_random():
    if not entries:
        return jsonify({"error": "No entries found"}), 404
    return jsonify(random.choice(entries))

@app.route("/api/get-motivation", methods=['GET'])
def get_motivation():
    motivation = [
        "You are a great person", "You are doing great", "You are amazing", "You are awesome", "You are the best"
    ]
    return jsonify(random.choice(motivation))

if __name__ == '__main__':
    app.run(debug=True)
