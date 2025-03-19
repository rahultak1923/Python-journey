from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
@app.route('/signin', methods=['POST'])
def signin():
    print(request.data)

    try: 
        data = request.get_json()  # Get JSON data from the request
        print(data)
    except Exception as e :
        print(str(e))
    data = None
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400
    
    full_name = data.get('fullName')
    email = data.get('email')
    password = data.get('password')

    # Validate required fields
    if not full_name:
        return jsonify({"error": "Full Name is required"}), 400
    if not email:
        return jsonify({"error": "Email is required"}), 400
    if not password:
        return jsonify({"error": "Password is required"}), 400

    return jsonify({
        "message": "User registered successfully!",
        "user": {
            "fullName": full_name,
            "email": email
        }
    }), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
