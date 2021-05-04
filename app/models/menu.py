from .db import db
from .menu_items import menu_items

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))

    menu_items = db.relationship("Item", secondary=menu_items)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "restaurant_id": self.restaurant_id,
            "menu_items": [menu_item.to_dict() for menu_item in self.menu_items]
        }