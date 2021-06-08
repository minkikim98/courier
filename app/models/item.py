from .db import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Numeric(asdecimal=False), nullable=False)
    image_url = db.Column(db.String(2048), nullable=True)

    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "image_url": self.image_url,
            "restaurant_id": self.restaurant_id,
        }
