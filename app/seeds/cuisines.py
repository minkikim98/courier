from app.models import db, Cuisine


def seed_cuisines():

    # 1
    convenience = Cuisine(name='Convenience')
    db.session.add(convenience)

    fast = Cuisine(name='Fast Food')
    db.session.add(fast)

    chicken = Cuisine(name='Chicken')
    db.session.add(chicken)

    desserts = Cuisine(name='Desserts')
    db.session.add(desserts)

    # 5
    healthy = Cuisine(name='Healthy')
    db.session.add(healthy)

    asian = Cuisine(name='Asian')
    db.session.add(asian)

    mexican = Cuisine(name='Mexican')
    db.session.add(mexican)

    burgers = Cuisine(name='Burgers')
    db.session.add(burgers)

    breakfast = Cuisine(name='Breakfast')
    db.session.add(breakfast)

    # 10
    sandwiches = Cuisine(name='Sandwiches')
    db.session.add(sandwiches)

    chinese = Cuisine(name='Chinese')
    db.session.add(chinese)

    japanese = Cuisine(name='Japanese')
    db.session.add(japanese)

    pizza = Cuisine(name='Pizza')
    db.session.add(pizza)

    vegan = Cuisine(name='Vegan')
    db.session.add(vegan)

    # 15
    thai = Cuisine(name='Thai')
    db.session.add(thai)

    vietnamese = Cuisine(name='Vietnamese')
    db.session.add(vietnamese)

    alcohol = Cuisine(name='Alcohol')
    db.session.add(alcohol)
    

    db.session.commit()


def undo_cuisines():
    db.session.execute('TRUNCATE cuisines RESTART IDENTITY CASCADE;')
    db.session.commit()
