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

    # 1
    panda = Restaurant(name='Panda Express', address='5150 Cherry Ave, San Jose, CA 95118', 
        description="Fast-food chain for Chinese standards, including some health-conscious options.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/42492.jpg")
    panda.cuisines.append(chinese)
    panda.cuisines.append(asian)
    db.session.add(panda)

    #2
    mcd = Restaurant(name='McDonald\'s', address='1365 Blossom Hill Rd, San Jose, CA 95118', 
        description="Classic, long-running fast-food chain known for its burgers, fries & shakes.", 
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/5579.png")
    mcd.cuisines.append(fast)
    mcd.cuisines.append(burgers)
    # mcd.cuisines.append(desserts)
    db.session.add(mcd)

    #3
    poki = Restaurant(name='Poki Time', address='2101 Lombard St, San Francisco, CA 94123', 
        description="Hawaiian poke bowls are made-to-order at this local chain link also serving a range of desserts.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/349186.jpg")
    poki.cuisines.append(healthy)
    poki.cuisines.append(asian)
    poki.cuisines.append(japanese)
    db.session.add(poki)

    #4
    tony = Restaurant(name='Tony\'s Pizza Napoletana', address='1570 Stockton St, San Francisco, CA 94133', 
        description="Bustling Italian eatery with varied pizza options from coal-fired to Roman-style, plus beer on tap.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/193224.jpg")
    tony.cuisines.append(pizza)
    tony.cuisines.append(italian)
    db.session.add(tony)

    #5
    kfc = Restaurant(name='Kentucky Fried Chicken', address='691 Eddy St, San Francisco, CA 94109', 
        description="Fast-food chain known for its buckets of fried chicken, plus wings & sides.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/1e869531-be3a-4c1a-a4c1-271e81113b1e.jpg")
    kfc.cuisines.append(chicken)
    kfc.cuisines.append(fast)
    db.session.add(kfc)

    #6
    honey = Restaurant(name='Honey Honey Cafe & Crepery', address='599 Post St, San Francisco, CA 94102', 
        description="Diners order at the counter at this casual, cheery spot that cooks up a mix of crêpes & cafe fare.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/fa17869e-208a-4604-94e8-81b2bf70fd4f.466")
    honey.cuisines.append(breakfast)
    db.session.add(honey)

    #7
    smash = Restaurant(name='Smashburger', address='2300 16th St Suite 293, San Francisco, CA 94103', 
        description="Counter-serve chain featuring signature smashed burgers, plus sides & shakes.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/43726.jpg")
    smash.cuisines.append(burgers)
    smash.cuisines.append(fast)
    db.session.add(smash)

    #8
    subway = Restaurant(name='Subway', address='550B C St, San Francisco, CA 94158', 
        description="Casual counter-serve chain for build-your-own sandwiches & salads, with health-conscious options.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/3720.jpg")
    subway.cuisines.append(fast)
    subway.cuisines.append(healthy)
    db.session.add(subway)

    #9
    hinodeya = Restaurant(name='Hinodeya Ramen Downtown', address='680 Clay St, San Francisco, CA 94111', 
        description="",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/9d75fc4f-44b7-485e-82df-4204916745af.JPG")
    hinodeya.cuisines.append(asian)
    hinodeya.cuisines.append(japanese)
    db.session.add(hinodeya)

    #10
    lers = Restaurant(name='Lers Ros Thai', address='730 Larkin St, San Francisco, CA 94109', 
        description="Popular late-night Thai spot with long menu of exotic game specials & more traditional Thai dishes.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/21157.jpg")
    lers.cuisines.append(thai)
    lers.cuisines.append(asian)
    db.session.add(lers)

    #11
    chipotle = Restaurant(name='Chipotle', address='211 Sutter St, San Francisco, CA 94104', 
        description="Fast-food chain offering Mexican fare, including design-your-own burritos, tacos & bowls.",
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=1920,format=auto,quality=50/https://cdn.doordash.com/media/store/header/8b48c653-0eca-40bb-8e47-6fd4ac0f75b5.jpg")
    chipotle.cuisines.append(mexican)
    chipotle.cuisines.append(healthy)
    db.session.add(chipotle)

    db.session.commit()


def undo_restaurants():
    db.session.execute('TRUNCATE restaurants RESTART IDENTITY CASCADE;')
    db.session.commit()
