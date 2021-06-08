from flask import Blueprint, jsonify
from app.models import Restaurant, Cart, Item, CartItem, Cuisine, Tag, db

restaurant_routes = Blueprint('restaurants', __name__)

@restaurant_routes.route("/")
def get_all_restaurants():
    all_restaurants = Restaurant.query.all()
    return { "restaurants": { restaurant.id : restaurant.to_simple_dict() for restaurant in all_restaurants } }

@restaurant_routes.route("/<restaurant_id>")
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)
    return restaurant.to_dict()

# @restaurant_routes.route("/cuisines/<cuisine_id>")
# def get_restaurants_for_cuisine(cuisine_id):
#     cuisine = Cuisine.query.get(cuisine_id)
#     return { "cuisine_filter_id" : cuisine_id, "tag_filter_id" : 0, "restaurants": { restaurant.id : restaurant.to_simple_dict() for restaurant in cuisine.restaurants } }

# @restaurant_routes.route("/tags/<tag_id>")
# def get_restaurants_for_tag(tag_id):
#     tag = Tag.query.get(tag_id)
#     return { "cuisine_filter_id" : 0, "tag_filter_id" : tag_id, "restaurants": { restaurant.id : restaurant.to_simple_dict() for restaurant in tag.restaurants } }