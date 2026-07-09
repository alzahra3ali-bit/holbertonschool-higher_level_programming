from flask import Flask, jsonify, request



app = Flask(__name__)

users = {}

@app.route('/')

def home():

    return "Welcome to the Flask API!"

@app.route('/status')

def status():

    return "OK"

@app.route('/data')

def get_data():

    all_usernames = list(users.keys())

    return jsonify(all_usernames)

@app.route('/users/<username>')

def get_info(username):

    if username in users:

        return jsonify(users[username])

    else:

        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])

def add_user():

    data = request.get_json(silent = True)

    if data is None:

        return jsonify({"error":"Invalid JSON"}), 400

    usern = data.get('username')

    if not usern:

        return jsonify({"error":"Username is required"}), 400

    if usern in users:

        return jsonify({"error":"Username already exists"}), 409

    users[usern] = data

    massag = {

        "message": "User added",

        "user": data

            }

    return jsonify(massag), 201
