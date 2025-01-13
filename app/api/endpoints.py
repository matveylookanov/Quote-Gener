from flask import Blueprint, jsonify, request
from app.models import Quote
from app import db

api_bp = Blueprint("api", __name__)

@api_bp.route("/quote/random", methods=["GET"])
def random_quote():
    quote = Quote.query.order_by(db.func.random()).first()
    if quote:
        return jsonify(quote.to_dict())
    return jsonify({"error": "No quotes available"}), 404

@api_bp.route("/quote", methods=["POST"])
def add_quote():
    data = request.get_json()
    if not data or "text" not in data or "category" not in data:
        return jsonify({"error": "Invalid data"}), 400

    quote = Quote(
        text=data["text"],
        author=data.get("author", "Unknown"),
        category=data["category"]
    )
    db.session.add(quote)
    db.session.commit()

    return jsonify(quote.to_dict()), 201
