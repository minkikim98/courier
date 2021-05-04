from .db import db 
from .restaurant_cuisines import restaurant_cuisines

class Cuisine(db.Model):
    __tablename__ = "cuisines"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    restaurants = db.relationship("Restaurant", back_populates="cuisines", secondary=restaurant_cuisines)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "restaurants": [restaurant.to_dict() for restaurant in self.restaurants]
        }