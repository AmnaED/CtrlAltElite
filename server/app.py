from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
from pymongo import MongoClient
from hardware import hardwareSet
from user import User
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

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = data.get("user_id")
    name = data.get("name")
    password = data.get("password")

    if not user_id or not name or not password:
        return jsonify({"error: Missing required fields"}), 400

    if user_collection.find_one({"user_id": user_id}):
        return jsonify({"error": "User already exists"}), 400
    
    new_user = User(user_id=user_id, name=name, password=password)
    user_collection.insert_one(new_user.to_dict())
    return jsonify({"message": "User created successfully"}), 201

@app.route("/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user_data = user_collection.find_one({"user_id": user_id}, {"_id": 0})
    if user_data:
        user = User(user_data=user_data, encrypted=True)
        return jsonify(user.to_dict())
    else:
        return jsonify({"error": "User not found"}), 404

@app.route("/users/<user_id>/projects", methods=["POST"])
def add_user_to_project(user_id):
    data = request.get_json()
    project_id = data.get("project_id")

    if not project_id:
        return jsonify({"error": "Project ID is required"}), 400

    user_data = user_collection.find_one({"user_id": user_id})
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    user = User(user_data=user_data, encrypted=True)
    user.add_to_project(project_id)
    user_collection.update_one({"user_id": user_id}, {"$set": user.to_dict()})
    
    return jsonify({"message": "User added to project successfully"}), 200

@app.route("/users/<user_id>/projects", methods=["DELETE"])
def remove_user_from_project(user_id):
    data = request.get_json()
    project_id = data.get("project_id")

    if not project_id:
        return jsonify({"error": "Project ID is required"}), 400
        
    user_data = user_collection.find_one({"user_id": user_id})
    if not user_data:
        return jsonify({"error": "User not found"}), 404

    user = User(user_data=user_data, encrypted=True)
    user.remove_from_project(project_id)
    user_collection.update_one({"user_id": user_id}, {"$set": user.to_dict()})
    
    return jsonify({"message": "User removed from project successfully"}), 200



if __name__ == "__main__":
    app.run(debug=True)