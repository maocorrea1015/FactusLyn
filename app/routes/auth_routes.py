from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong desde LabsFactus"}), 200
