from .db import db
from .menu_items import menu_items

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))

    menu_items = db.relationship("Item", secondary=menu_items)