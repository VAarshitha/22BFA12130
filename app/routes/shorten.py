# app/routes/shorten.py
from flask import Blueprint, request, jsonify
import hashlib

api = Blueprint('api', __name__)

url_db = {}

@api.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")
    
    if not original_url:
        return jsonify({"error": "Missing URL"}), 400

    short_code = hashlib.md5(original_url.encode()).hexdigest()[:6]
    url_db[short_code] = original_url

    return jsonify({
        "original_url": original_url,
        "short_url": f"http://localhost:5000/api/{short_code}"
    }), 200

@api.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    original_url = url_db.get(short_code)
    if original_url:
        return jsonify({"redirect_to": original_url})
    return jsonify({"error": "URL not found"}), 404
