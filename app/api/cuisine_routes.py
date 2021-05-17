from flask import Blueprint
from app.models import Cuisine

cuisine_routes = Blueprint("cuisines", __name__)

@cuisine_routes.route("/")
def get_cuisines():
    all_cuisines = Cuisine.query.all()
    return { cuisine.id : cuisine.to_dict() for cuisine in all_cuisines }