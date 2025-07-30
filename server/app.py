from flask import Flask, jsonify
from flask_cors import CORS
from encryption import encrypt, decrypt

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/encrypt", methods=["POST"])
def encrypt_route():
    data = request.get_json()
    text = data.get("text")

    if not text:
        return jsonify({"error": "Missing required fields"}), 400

    N = 3 # fixed key for encryption
    D = 1 # fixed direction for encryption
    
    encrypted_text = encrypt(text, N, D)
    return jsonify({"encrypted": encrypted_text})

@app.route("/decrypt", methods=["POST"])
def decrypt_route():
    data = request.get_json()
    encrypted_text = data.get("text")

    if not encrypted_text:
        return jsonify({"error": "Missing required fields"}), 400

    N = 3
    D = 1
    
    decrypted_text = decrypt(encrypted_text, N, D)
    return jsonify({"decrypted": decrypted_text})

if __name__ == "__main__":
    app.run(debug=True)