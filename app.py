#!/usr/bin/python
from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_users, get_user_by_id, insert_user, update_user, delete_user

# ----------------------------
# Flask App Setup
# ----------------------------
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# ----------------------------
# API Endpoints
# ----------------------------

# Get all users
@app.route('/api/users', methods=['GET'])
def api_get_users():
    return jsonify(get_users())

# Get a single user by ID
@app.route('/api/users/<int:user_id>', methods=['GET'])
def api_get_user(user_id):
    return jsonify(get_user_by_id(user_id))

# Add a new user
@app.route('/api/users/add', methods=['POST'])
def api_add_user():
    user = request.get_json()
    return jsonify(insert_user(user))

# Update an existing user
@app.route('/api/users/update', methods=['PUT'])
def api_update_user():
    user = request.get_json()
    return jsonify(update_user(user))

# Delete a user by ID
@app.route('/api/users/delete/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    return jsonify(delete_user(user_id))

# ----------------------------
# Run Flask App
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
