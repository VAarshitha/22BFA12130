from flask import Blueprint, jsonify
from .services import get_companies

api = Blueprint('api', __name__)

@api.route('/companies', methods=['GET'])
def companies():
    try:
        data = get_companies()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
