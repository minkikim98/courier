from .db import db

menu_items = db.Table(
    "menu_items",
    db.Model.metadata,
    db.Column("menu_id", db.Integer, db.ForeignKey(
        "menus.id"), primary_key=True),
    db.Column("item_id", db.Integer, db.ForeignKey(
        "items.id"), primary_key=True)
)