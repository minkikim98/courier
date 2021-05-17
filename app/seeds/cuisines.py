from app.models import db, Cuisine


def seed_cuisines():

    # 1
    # convenience = Cuisine(name='Convenience', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Convenience.jpg")
    # db.session.add(convenience)

    fast = Cuisine(name='Fast Food', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Fast+Food.jpg")
    db.session.add(fast)

    # chicken = Cuisine(name='Chicken', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Chicken.jpg")
    # db.session.add(chicken)

    # desserts = Cuisine(name='Desserts', image_url="")
    # db.session.add(desserts)

    # # 5
    # healthy = Cuisine(name='Healthy')
    # db.session.add(healthy)

    asian = Cuisine(name='Asian', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Asian.jpg")
    db.session.add(asian)

    # mexican = Cuisine(name='Mexican')
    # db.session.add(mexican)

    burgers = Cuisine(name='Burgers', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Burgers.jpg")
    db.session.add(burgers)

    # breakfast = Cuisine(name='Breakfast')
    # db.session.add(breakfast)

    # # 10
    # sandwiches = Cuisine(name='Sandwiches')
    # db.session.add(sandwiches)

    chinese = Cuisine(name='Chinese', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Chinese.jpg")
    db.session.add(chinese)

    # japanese = Cuisine(name='Japanese')
    # db.session.add(japanese)

    # pizza = Cuisine(name='Pizza')
    # db.session.add(pizza)

    # vegan = Cuisine(name='Vegan')
    # db.session.add(vegan)

    # # 15
    # thai = Cuisine(name='Thai')
    # db.session.add(thai)

    # vietnamese = Cuisine(name='Vietnamese')
    # db.session.add(vietnamese)

    # alcohol = Cuisine(name='Alcohol')
    # db.session.add(alcohol)
    

    db.session.commit()


def undo_cuisines():
    db.session.execute('TRUNCATE cuisines RESTART IDENTITY CASCADE;')
    db.session.commit()
