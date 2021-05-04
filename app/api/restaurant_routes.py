from flask import Blueprint, jsonify
from app.models import Restaurant

restaurant_routes = Blueprint('restaurants', __name__)

@restaurant_routes.route("/")
def get_restaurants():
    panda = Restaurant.query.get(1)
    return panda.to_dict()