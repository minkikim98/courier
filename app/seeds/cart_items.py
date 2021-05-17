from app.models import db, CartItem, Item, Cart


def seed_cart_items():
    user_cart = Cart.query.get(1)
    plate = Item.query.get(1)

    plate_item = CartItem(quantity=3)
    plate_item.item = plate
    user_cart.cart_items.append(plate_item)

    db.session.add(plate_item)

    bigger_plate = Item.query.get(2)

    bigger_plate_item = CartItem(quantity=1)
    bigger_plate_item.item = bigger_plate
    user_cart.cart_items.append(bigger_plate_item)

    db.session.add(bigger_plate_item)
    db.session.commit()




def undo_cart_items():
    db.session.execute('TRUNCATE cart_items RESTART IDENTITY CASCADE;')
    db.session.commit()
