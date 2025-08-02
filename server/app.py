from flask import Flask, jsonify
from flask_cors import CORS
from encryption import encrypt, decrypt
from dotenv import load_dotenv
from pymongo import MongoClient
import os

# Load environment variables from .env
load_dotenv()
from dotenv import load_dotenv
from pymongo import MongoClient
from hardware import hardwareSet
import os

# Load environment variables from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/encrypt", methods=["POST"])
def encrypt_route():
    data = request.get_json()
    text = data.get("text")

    if not text or N is None or D is None:
        return jsonify({"error": "Missing required fields"}), 400

    N = 3 # fixed key for encryption
    N = 1 # fixed direction for encryption
    
    encrypted_text = encrypt(text, N, D)
    return jsonify({"encrypted": encrypted_text})

@app.route("/decrypt", methods=["POST"])
def decrypt_route():
    data = request.get_json()
    encrypted_text = data.get("text")
    N = 3
    D = 1

    if not encrypted_text or N is None or D is None:
        return jsonify({"error": "Missing required fields"}), 400
    
    decrypted_text = decrypt(encrypted_text, N, D)
    return jsonify({"decrypted": decrypted_text})

@app.route("/hardware/<int:hardware_id>/capacity", methods=["GET"])
def get_hardware_capacity(hardware_id):
    hardware_set = hardwareSet()
    hardware = resources_collection.find_one(
        {"hardware_id": hardware_id},
        {"_id": 0, "total_capacity": 1}
    )
    if hardware:
        hardware_set.initialize_capacity(hardware)
        capacity = hardware_set.get_capacity()
        return jsonify({capacity})
    else:
        return jsonify("Hardware not found")

@app.route("/hardware/<int:hardware_id>", methods=["GET"])
def get_hardware_availability(hardware_id):
    hardware_set = hardwareSet()
    hardware = resources_collection.find_one(
        {"hardware_id": hardware_id},
        {"_id": 0, "available": 1}
    )
    if hardware:
        hardware_set.initialize_availability(hardware)
        availability = hardware_set.get_availability()
        jsonify({availability})
    else:
        return jsonify("Hardware not found")


if __name__ == "__main__":
    app.run(debug=True)