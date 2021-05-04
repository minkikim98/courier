from .db import db

class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Numeric(asdecimal=False), nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurants.id"))
