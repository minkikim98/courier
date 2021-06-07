from .db import db
from .restaurant_cuisines import restaurant_cuisines
from .restaurant_tags import restaurant_tags

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=False)
    image_url = db.Column(db.String(300), nullable=False)

    cuisines = db.relationship("Cuisine", back_populates="restaurants", secondary=restaurant_cuisines)
    tags = db.relationship("Tag", back_populates="restaurants", secondary=restaurant_tags)
    menus = db.relationship("Menu")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
            "image_url": self.image_url,
            "cuisines": [{"cuisine_id": cuisine.id, "cuisine_name": cuisine.name} for cuisine in self.cuisines],
            "tags": [{"tag_id": tag.id, "tag_name": tag.name} for tag in self.tags],
            "menus": [menu.to_dict() for menu in self.menus]
        }

    def to_simple_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
            "image_url": self.image_url,
            "cuisines": [{"cuisine_id": cuisine.id, "cuisine_name": cuisine.name} for cuisine in self.cuisines],
            "tags": [{"tag_id": tag.id, "tag_name": tag.name} for tag in self.tags],
        }
