from flask import Blueprint, jsonify, request
from app.models import Cart, Item, CartItem, db
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
        body = request.get_json()
        item_id = int(body["item_id"])

        user_cart = Cart.query.get(current_user.id)
        item = Item.query.get(item_id)
        cart_item = CartItem(quantity=1)
        cart_item.item = item
        user_cart.cart_items.append(cart_item)

        db.session.add(cart_item)
        db.session.commit()
        return user_cart.to_dict()
        
    return {'errors': ['Unauthorized']}

