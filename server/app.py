from flask import Flask, jsonify, request
from flask_cors import CORS
from encryption import encrypt, decrypt
from dotenv import load_dotenv
from pymongo import MongoClient
from hardware import hardwareSet
import os

# Load environment variables from .env
load_dotenv()

# Initialize hardware set
hardware_set = hardwareSet()

app = Flask(__name__)
CORS(app)

# Get MongoDB password and connect to database
mongo_pass = os.getenv("MONGO_PASSWORD")
link = f"mongodb+srv://ranyae:{mongo_pass}@apad-project.qvgsgr3.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(link)

# Accessing collections
resource_db = client["resource-management-db"]
resources_collection = resource_db["resources"]
project_db = client["project-table-db"]
project_collection = project_db["project-table"]
user_db = client["user-management-db"]
user_collection = user_db["user-management"]


@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask!"})

@app.route("/hardware/<int:hardware_id>/capacity", methods=["GET"])
def get_hardware_capacity(hardware_id):
    hardware = resources_collection.find_one(
        {"hardware_id": hardware_id},
        {"_id": 0, "total_capacity": 1}
    )
    if hardware:
        hardware_set.initialize_capacity(hardware)
        capacity = hardware_set.get_capacity()
        return jsonify({"capacity": capacity})

    else:
        return jsonify({"error": "Hardware not found"})

@app.route("/hardware/<int:hardware_id>/availability", methods=["GET"])
def get_hardware_availability(hardware_id):
    hardware = resources_collection.find_one(
        {"hardware_id": hardware_id},
        {"_id": 0, "available": 1}
    )
    if hardware:
        hardware_set.initialize_availability(hardware)
        availability = hardware_set.get_availability()
        return jsonify({"availability": availability})

    else:
        return jsonify({"error": "Hardware not found"})
    
@app.route("/hardware/checkout", methods=["POST"])
def checkout_hardware():
    data = request.get_json()
    qty = data.get("qty")
    project_id = data.get("project_id")
    hardware_id = data.get("hardware_id")

    result = hardware_set.check_out(qty, project_id, hardware_id)
    return jsonify({"result": result})

@app.route("/hardware/checkin", methods=["POST"])
def checkin_hardware():
    data = request.get_json()
    qty = data.get("qty")
    project_id = data.get("project_id")
    hardware_id = data.get("hardware_id")

    result = hardware_set.check_in(qty, project_id, hardware_id)
    return jsonify({"result": result})


if __name__ == "__main__":
    app.run(debug=True)