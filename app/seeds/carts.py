from app.models import db, Cart


def seed_carts():
    demo_cart = Cart(user_id=1)
    demo_cart.restaurant_id = 1
    db.session.add(demo_cart)
    db.session.commit()


def undo_carts():
    db.session.execute('TRUNCATE carts RESTART IDENTITY CASCADE;')
    db.session.commit()
