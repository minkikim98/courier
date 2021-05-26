from app.models import db, Cuisine


def seed_cuisines():

    fast = Cuisine(name='Fast Food', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Fast+Food.jpg")
    db.session.add(fast)

    asian = Cuisine(name='Asian', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Asian.jpg")
    db.session.add(asian)
    
    burgers = Cuisine(name='Burgers', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Burgers.jpg")
    db.session.add(burgers)

    chinese = Cuisine(name='Chinese', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Chinese.jpg")
    db.session.add(chinese)

    healthy = Cuisine(name='Healthy', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Healthy.jpg")
    db.session.add(healthy)

    breakfast = Cuisine(name='Breakfast', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Breakfast.jpg")
    db.session.add(breakfast)

    thai = Cuisine(name='Thai', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Thai.jpg")
    db.session.add(thai)

    chicken = Cuisine(name='Chicken', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Chicken.jpg")
    db.session.add(chicken)

    mexican = Cuisine(name='Mexican', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Mexican.jpg")
    db.session.add(mexican)

    japanese = Cuisine(name='Japanese', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Japanese.jpg")
    db.session.add(japanese)

    italian = Cuisine(name='Italian', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Italian.jpg")
    db.session.add(italian)

    pizza = Cuisine(name='Pizza', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Pizza.jpg")
    db.session.add(pizza)

    # convenience = Cuisine(name='Convenience', image_url="https://dannydash-seeds.s3-us-west-1.amazonaws.com/Convenience.jpg")
    # db.session.add(convenience)


    # desserts = Cuisine(name='Desserts', image_url="")
    # db.session.add(desserts)



    # sandwiches = Cuisine(name='Sandwiches')
    # db.session.add(sandwiches)




    # vegan = Cuisine(name='Vegan')
    # db.session.add(vegan)

    # # 15

    # vietnamese = Cuisine(name='Vietnamese')
    # db.session.add(vietnamese)

    # alcohol = Cuisine(name='Alcohol')
    # db.session.add(alcohol)
    

    db.session.commit()


def undo_cuisines():
    db.session.execute('TRUNCATE cuisines RESTART IDENTITY CASCADE;')
    db.session.commit()
