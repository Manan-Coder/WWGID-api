from flask import Flask,jsonify,request
from datetime import datetime
import random

app = Flask(__name__)
entries = []
@app.route("/api/add", methods=['POST'])
def add():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}),400
    entry = data.get("entry")
    if not entry:
        return jsonify({"error": "No entry provided"}),400
    new_entry = {
        'id': len(entries)+1,
        'entr   y': entry,
        'date': datetime.now().strftime("%Y-%m-%d") 
    }
    entries.append(new_entry)
    return jsonify({'message' : 'Entry added successfully','id': new_entry['id']})

@app.route("/api/get-all", methods=['GET'])
def get_entries():
    if not entries:
        return jsonify({"error": "No entries found"}),404
    return jsonify(entries)

@app.route("/api/get-random", methods=['GET'])
def get_random():
    if not entries:
        return jsonify({"error": "No entries found"}),404
    return jsonify(random.choice(entries))

@app.route("/api/get-motivation", methods=['GET'])
def get_motivation():
    motivation = [
        "You are a great person",
        "You are doing great",
        "You are amazing",
        "You are awesome",
        "You are the best",
        "You are a star",
        "You are a winner",
        "You are a champion",
        "You are a warrior",
        "You are a hero",
        "You are a legend",
        "You are a genius",
        "You are a master",
        "You are a wizard",
        "You are a magician",
        "You are a miracle",
        "You are a blessing",
        "You are a gift",
        "You are a treasure",
        "You are a diamond",
        "You are a jewel",
        "You are a pearl",
        "You are a gold",
        "You are a silver",
        "You are a bronze",
        "You are a platinum",
        "You are a diamond",
        "You are a gem",
        "You are a rockstar",
        "You are a superstar",
        "You are a megastar",
        "You are a supernova",
        "You are a galaxy",
        "You are a universe",
        "You are a cosmos",
        "You are a space",
        "You are a time",
        "You are a dimension",
        "You are a reality",
        "You are a dream",
        "You are a vision",
        "You are a mission",
        "You are a purpose",
        "You are a goal",
        "You are a target",
        "You are a destination",
        "You are a journey",
        "You are a path",
        "You are a road",
        "You are a street",
        "You are a lane",
        "You are a way",
        "You are a bridge",
        "You are a tunnel",
        "You are a mountain",
        "You are a hill",
        "You are a valley",
        "You are a river",
        "You are a stream",
        "You are a lake",
        "You are a sea",
        "You are an ocean",
        "You are a sky",
        "You are a cloud",
        "You are a rain",
        "You are a rainbow",
        "You are a sun",
        "You are a moon",
        "You are a star",
        "You are a planet",
        "You are a galaxy",
        "You are a universe",
        ]
    return jsonify(random.choice(motivation))

if __name__ == '__main__':
    app.run(debug=True)
