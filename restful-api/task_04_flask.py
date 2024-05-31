#!/usr/bin/python3
""" Nameless Module for Task 4 """

from flask import Flask, jsonify, request, abort

# Step 1
app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """ Prints welcome string """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """ Returns JSON data """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """ Prints OK """
    return "OK"


@app.route("/users/<username>")
def users_specific(username):
    """ Get specified """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    output = users[username]
    output["username"] = username

    return jsonify(output)


@app.route("/add_user", methods=["POST"])
def add_user():
    """ adds a new user to the dict """
    if request.get_json() is None:
        abort(400, "Not a JSON")

    req_data = request.get_json()

    if "username" not in req_data:
        return jsonify({"error": "Username is required"}), 400

    users[req_data["username"]] = {
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }

    output = {
        "username": req_data["username"],
        "name": req_data["name"],
        "age": req_data["age"],
        "city": req_data["city"]
    }
    return jsonify({"message": "User added", "user": output}), 201


# Set debug=True for the server to auto-reload when there are changes
if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
