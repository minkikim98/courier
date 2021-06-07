from .db import db 
from .restaurant_tags import restaurant_tags

class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    restaurants = db.relationship("Restaurant", back_populates="tags", secondary=restaurant_tags)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "restaurants": [restaurant.to_dict() for restaurant in self.restaurants]
        }