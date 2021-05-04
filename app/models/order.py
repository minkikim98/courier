from .db import db
import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    placed_on = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now())
    completed = db.Column(db.Boolean)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    order_items = db.relationship("OrderItem", back_populates="orders")