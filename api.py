from flask import Flask, jsonify, request
import sqlite3
app = Flask(__name__)
con = sqlite3.connect("data/db.sqlite", check_same_thread=False)
cur = con.cursor()
con.execute('CREATE TABLE IF NOT EXISTS scores(id INTEGER PRIMARY KEY AUTOINCREMENT,userName VARCHAR(15) NOT NULL, score BIGINT UNSIGNED NOT NULL)')

@app.route('/api/score', methods=['POST'])
def new_score():
    print(request.get_json())
    if not request.json or 'score' not in request.json or 'userName' not in request.json:
        return jsonify({'msg': 'Bad request'}), 400
    username = request.json['userName']
    score = str(request.json['score'])
    result = con.execute('INSERT INTO scores (name, score) VALUES('+str(request.json['userName'])+', '+str(request.json['score'])+')')
    
    return jsonify({'result': result}), 201
if __name__ == '__main__':
    app.run(debug=True)
