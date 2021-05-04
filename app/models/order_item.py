from .db import db 

class OrderItem(db.Model):
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    orders = db.relationship("Order", back_populates="order_items")