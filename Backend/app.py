from flask import Flask, request, jsonify
from flask_cors import CORS
from db.query import insert_user, login_user

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# 🔐 Signup Route
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    useremail = data.get('useremail')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')

    if not all([name, useremail, password, firstname, lastname]):
        return jsonify({'status': 'error', 'message': 'All fields are required.'}), 400

    success = insert_user(name, useremail, password, firstname, lastname)

    if success:
        return jsonify({'status': 'success', 'message': 'User registered successfully.'}), 201
    else:
        return jsonify({'status': 'error', 'message': 'Registration failed. Email may already exist.'}), 400

# 🔐 Login Route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()

    useremail = data.get('useremail')
    password = data.get('password')

    if not all([useremail, password]):
        return jsonify({'status': 'error', 'message': 'Email and password are required.'}), 400

    user = login_user(useremail, password)

    if user:
        return jsonify({
            'status': 'success',
            'message': 'Login successful.',
            'user': {
                'id': user['id'],
                'name': user['name'],
                'useremail': user['useremail'],
                'firstname': user['firstname'],
                'lastname': user['lastname'],
                'account_status': user['account_status']
            }
        }), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid email or password.'}), 401

if __name__ == '__main__':
    app.run(debug=True)
