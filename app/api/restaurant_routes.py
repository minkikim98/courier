from flask import Blueprint, jsonify
from app.models import Restaurant, Cart, Item, CartItem, db

restaurant_routes = Blueprint('restaurants', __name__)

@restaurant_routes.route("/")
def get_restaurants():
    all_restaurants = Restaurant.query.all()
    return { restaurant.id : restaurant.to_dict() for restaurant in all_restaurants }

@restaurant_routes.route("/test-add-cart")
def test_cart():
    panda_cart = Cart.query.get(1)
    plate = Item.query.get(1)

    plate_item = CartItem(quantity=3)
    plate_item.item = plate
    panda_cart.cart_items.append(plate_item)

    db.session.add(plate_item)
    db.session.commit()
    return {}