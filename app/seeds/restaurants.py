from app.models import db, Restaurant, Cuisine


def seed_restaurants():

    fast = Cuisine.query.get(1)
    # desserts = Cuisine.query.get(4)
    asian = Cuisine.query.get(2)
    burgers = Cuisine.query.get(3)
    chinese = Cuisine.query.get(4)

    
    panda = Restaurant(name='Panda Express', address='5150 Cherry Ave, San Jose, CA 95118', 
        description="Fast-food chain for Chinese standards, including some health-conscious options.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/42492.jpg")
    panda.cuisines.append(chinese)
    panda.cuisines.append(asian)
    db.session.add(panda)

    mcd = Restaurant(name='McDonald\'s', address='1365 Blossom Hill Rd, San Jose, CA 95118', 
        description="Classic, long-running fast-food chain known for its burgers, fries & shakes.", 
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/5579.png")
    mcd.cuisines.append(fast)
    mcd.cuisines.append(burgers)
    # mcd.cuisines.append(desserts)
    db.session.add(mcd)

    db.session.commit()


def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
