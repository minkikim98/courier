from flask import Blueprint, jsonify
from app.models import Cart, db
from flask_login import current_user

cart_routes = Blueprint('carts', __name__)

@cart_routes.route("/")
def get_cart_items():
    if current_user.is_authenticated:
        user_cart = Cart.query.get(current_user.id)
        return user_cart.to_dict()
    return {'errors': ['Unauthorized']}

@cart_routes.route("/", methods=["POST"])
def add_cart_item():
    if current_user.is_authenticated:
        user_cart = Cart.query.get(current_user.id)

