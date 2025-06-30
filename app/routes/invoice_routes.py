from flask import Blueprint, jsonify

invoice_bp = Blueprint('invoice', __name__)

@invoice_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({"message": "pong desde invoice module"}), 200
