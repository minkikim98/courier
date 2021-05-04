from app.models import db, Item


def seed_items():
    # Panda Express
    # Popular Items
    item1 = Item(name='Plate', description="Any 1 Side & 2 Entrees", price=10.45, restaurant_id=1)
    db.session.add(item1)

    item2 = Item(name='Bigger Plate', description="Any 1 Side & 3 Entrees", price=12.25, restaurant_id=1)
    db.session.add(item2)

    item3 = Item(name='Bowl', description="Any 1 Side & 1 Entree", price=8.65, restaurant_id=1)
    db.session.add(item3)

    item4 = Item(name='Kid\'s Meal', description="Any 1 Side & 1 Entree", price=7.70, restaurant_id=1)
    db.session.add(item4)

    item5 = Item(name="Family Meal", description="Any 2 Large Sides & 3 Large Entrees", price=34.80, restaurant_id=1)
    db.session.add(item5)

    # A La Carte
    item6 = Item(name="Wok Seared Steak & Shrimp", price=12.50, restaurant_id=1)
    db.session.add(item6)

    item7 = Item(name="Black Pepper Angus Steak", price=12.50, restaurant_id=1)
    db.session.add(item7)

    db.session.commit()


def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
