from .db import db
from .item import Item

class CartItem(db.Model):
    __tablename__ = "cart_items"
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"))
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))

    cart = db.relationship("Cart", back_populates="cart_items")
    item = db.relationship("Item")

    def to_dict(self):
        item = Item.query.get(self.item_id)
        return {
            "id": self.id,
            "quantity": self.quantity,
            "cart_id": self.cart_id,
            "item_id": self.item_id,
            "item_name": item.name
        }