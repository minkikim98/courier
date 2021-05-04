from .db import db
from .restaurant_cuisines import restaurant_cuisines

class Restaurant(db.Model):
    __tablename__ = 'restaurants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=False)

    cuisines = db.relationship("Cuisine", back_populates="restaurants", secondary=restaurant_cuisines)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "description": self.description,
            "cuisines": [{"cuisine_id": cuisine.id, "cuisine_name": cuisine.name} for cuisine in self.cuisines]
        }
