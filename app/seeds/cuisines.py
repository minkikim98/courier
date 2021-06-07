from app.models import db, Cuisine


def seed_cuisines():

    fast = Cuisine(name='Fast Food', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Fast%2BFood.jpeg")
    db.session.add(fast)

    asian = Cuisine(name='Asian', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Asian.jpeg")
    db.session.add(asian)
    
    burgers = Cuisine(name='Burgers', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Burgers.jpeg")
    db.session.add(burgers)

    chinese = Cuisine(name='Chinese', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Chinese.jpeg")
    db.session.add(chinese)

    healthy = Cuisine(name='Healthy', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Healthy.jpeg")
    db.session.add(healthy)

    breakfast = Cuisine(name='Breakfast', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Breakfast.jpeg")
    db.session.add(breakfast)

    thai = Cuisine(name='Thai', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Thai.jpeg")
    db.session.add(thai)

    chicken = Cuisine(name='Chicken', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Chicken.jpeg")
    db.session.add(chicken)

    mexican = Cuisine(name='Mexican', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Mexican.jpeg")
    db.session.add(mexican)

    japanese = Cuisine(name='Japanese', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Japanese.jpeg")
    db.session.add(japanese)

    italian = Cuisine(name='Italian', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Italian.jpeg")
    db.session.add(italian)

    pizza = Cuisine(name='Pizza', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Pizza.jpeg")
    db.session.add(pizza)

    # convenience = Cuisine(name='Convenience', image_url="https://courier-images.s3-us-west-1.amazonaws.com/Convenience.jpeg")
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
