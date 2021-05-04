from .db import db

restaurant_cuisines = db.Table(
    "restaurant_cuisines",
    db.Model.metadata,
    db.Column("restaurant_id", db.Integer, db.ForeignKey(
        "restaurants.id"), primary_key=True),
    db.Column("cuisine_id", db.Integer, db.ForeignKey(
        "cuisines.id"), primary_key=True),
)