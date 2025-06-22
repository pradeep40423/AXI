from flask import Flask, request, jsonify
from flask_cors import CORS  # To allow cross-origin if frontend runs separately

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/process', methods=['POST'])
def process_request():
    data = request.get_json()  # Get JSON data from UI
    user_input = data.get('message', '')

    # Process the input (you can put your logic here)
    response_message = f"Received: {user_input}"

    # Return a JSON response
    return jsonify({'response': response_message})

if __name__ == '__main__':
    app.run(debug=True)
