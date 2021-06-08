from app.models import db, Menu, Item, Restaurant


def seed_menus():
    # Panda Express
    panda = Restaurant.query.get(1)
    panda_items = Item.query.filter(Item.restaurant_id == panda.id).all()

    popular = Menu(name='Popular Items', restaurant_id=1, description="The most commonly ordered items and dishes from this store.")
    alc = Menu(name='A La Carte', restaurant_id=1, description="Individual Entrees & Sides.")
    appetizers = Menu(name='Appetizers', restaurant_id=1, description="Something Extra with Your Meal")
    drinks = Menu(name='Drinks', restaurant_id=1, description="Add a Refreshing Beverage")

    for item in panda_items:
        if item.id < 6: popular.menu_items.append(item)
        elif item.id < 11: alc.menu_items.append(item)
        elif item.id < 13: appetizers.menu_items.append(item)
        else: drinks.menu_items.append(item)
    
    db.session.add(popular)
    db.session.add(alc)
    db.session.add(appetizers)
    db.session.add(drinks)

    db.session.commit()


def undo_menus():
    db.session.execute('TRUNCATE menus RESTART IDENTITY CASCADE;')
    db.session.commit()
