from app.models import db, Restaurant, Cuisine


def seed_restaurants():

    fast = Cuisine.query.get(1)
    asian = Cuisine.query.get(2)
    burgers = Cuisine.query.get(3)
    chinese = Cuisine.query.get(4)
    healthy = Cuisine.query.get(5)
    breakfast = Cuisine.query.get(6)
    thai = Cuisine.query.get(7)
    chicken = Cuisine.query.get(8)
    mexican = Cuisine.query.get(9)
    japanese = Cuisine.query.get(10)
    italian = Cuisine.query.get(11)
    pizza = Cuisine.query.get(12)

    
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

    poki = Restaurant(name='Poki Time', address='2101 Lombard St, San Francisco, CA 94123', 
        description="Hawaiian poke bowls are made-to-order at this local chain link also serving a range of desserts.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/349186.jpg")
    poki.cuisines.append(healthy)
    poki.cuisines.append(asian)
    poki.cuisines.append(japanese)
    db.session.add(poki)

    tony = Restaurant(name='Tony\'s Pizza Napoletana', address='1570 Stockton St, San Francisco, CA 94133', 
        description="Bustling Italian eatery with varied pizza options from coal-fired to Roman-style, plus beer on tap.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/193224.jpg")
    tony.cuisines.append(pizza)
    tony.cuisines.append(italian)
    db.session.add(tony)

    kfc = Restaurant(name='Kentucky Fried Chicken', address='691 Eddy St, San Francisco, CA 94109', 
        description="Fast-food chain known for its buckets of fried chicken, plus wings & sides.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/1e869531-be3a-4c1a-a4c1-271e81113b1e.jpg")
    kfc.cuisines.append(chicken)
    kfc.cuisines.append(fast)
    db.session.add(kfc)

    db.session.commit()


def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
