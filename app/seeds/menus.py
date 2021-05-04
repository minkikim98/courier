from app.models import db, Menu, Item, Restaurant


def seed_menus():
    # Panda Express
    panda = Restaurant.query.filter().first()
    panda_items = Item.query.filter(Item.restaurant_id == panda.id).all()

    popular = Menu(name='Popular Items', restaurant_id=1)
    alc = Menu(name='A La Carte', restaurant_id=1)
    for item in panda_items:
        if item.id < 6: popular.menu_items.append(item)
        else: alc.menu_items.append(item)
    db.session.add(popular)
    db.session.add(alc)

    db.session.commit()


def undo_menus():
    db.session.execute('TRUNCATE menus RESTART IDENTITY CASCADE;')
    db.session.commit()
