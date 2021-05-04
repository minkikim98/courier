from .db import db 

class CartItem(db.Model):
    __tablename__ = "cart_items"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    cart = db.relationship("Cart", back_populates="cart_items")
    item = db.relationship("Item")