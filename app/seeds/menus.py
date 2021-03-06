from app.models import db, Menu, Item, Restaurant


def seed_menus():
    # Panda Express
    panda = Restaurant.query.get(1)
    panda_items = Item.query.filter(Item.restaurant_id == panda.id).all()

    panda_popular = Menu(name='Popular Items', restaurant_id=1, description="The most commonly ordered items and dishes from this store.")
    panda_alc = Menu(name='A La Carte', restaurant_id=1, description="Individual Entrees & Sides.")
    panda_appetizers = Menu(name='Appetizers', restaurant_id=1, description="Something Extra with Your Meal")
    panda_drinks = Menu(name='Drinks', restaurant_id=1, description="Add a Refreshing Beverage")

    for item in panda_items:
        if item.id <= 5: panda_popular.menu_items.append(item)
        elif item.id <= 10: panda_alc.menu_items.append(item)
        elif item.id <= 12: panda_appetizers.menu_items.append(item)
        else: panda_drinks.menu_items.append(item)
    
    db.session.add(panda_popular)
    db.session.add(panda_alc)
    db.session.add(panda_appetizers)
    db.session.add(panda_drinks)


    # McDonald's
    mcd = Restaurant.query.get(2)
    mcd_items = Item.query.filter(Item.restaurant_id == mcd.id).all()

    mcd_popular = Menu(name='Most Popular', restaurant_id=2)
    mcd_combo = Menu(name='Combo Meals', restaurant_id=2)
    mcd_happy = Menu(name='Happy Meals', restaurant_id=2)
    mcd_cafe = Menu(name='McCafe', restaurant_id=2)
    mcd_sides = Menu(name='Fries, Sides, and More', restaurant_id=2)
    mcd_sweets = Menu(name='Sweets and Treats', restaurant_id=2)
    mcd_beverages = Menu(name='Beverages', restaurant_id=2)

    for item in mcd_items:
        item_id = item.id
        if item_id >= 17 and item_id <= 22: mcd_popular.menu_items.append(item)
        if (item_id >= 17 and item_id <= 19) or (item_id >= 23 and item_id <= 26): mcd_combo.menu_items.append(item)
        if item_id >= 27 and item_id <= 29: mcd_happy.menu_items.append(item)
        if item_id >= 30 and item_id <= 37: mcd_cafe.menu_items.append(item)
        if item_id == 38 or item_id == 21: mcd_sides.menu_items.append(item)
        if (item_id >= 39 and item_id <= 42) or item_id == 22: mcd_sweets.menu_items.append(item)
        if item_id >= 43 and item_id <= 49: mcd_beverages.menu_items.append(item)

    db.session.add(mcd_popular)
    db.session.add(mcd_combo)
    db.session.add(mcd_happy)
    db.session.add(mcd_cafe)
    db.session.add(mcd_sides)
    db.session.add(mcd_sweets)
    db.session.add(mcd_beverages)


    # Poki Time
    poki = Restaurant.query.get(3)
    poki_items = Item.query.filter(Item.restaurant_id == poki.id).all()

    poki_popular = Menu(name='Most Popular', description="The most commonly ordered items and dishes from this store.", restaurant_id=3)
    poki_bowls = Menu(name='Poki Bowls', restaurant_id=3)
    poki_humphry = Menu(name='Humphry Slocombe Ice Cream', restaurant_id=3)
    poki_leeuwen = Menu(name='Van Leeuwen Ice Cream', restaurant_id=3)
    poki_drinks = Menu(name='Drinks', restaurant_id=3)

    for item in poki_items:
        item_id = item.id
        if item_id >= 50 and item_id <= 55: poki_popular.menu_items.append(item)
        if (item_id >= 56 and item_id <= 57) or (item_id >= 50 and item_id <= 53): poki_bowls.menu_items.append(item)
        if item_id >= 58 and item_id <= 62: poki_humphry.menu_items.append(item)
        if item_id >= 63 and item_id <= 66: poki_leeuwen.menu_items.append(item)
        if item_id >= 67 and item_id <= 70: poki_drinks.menu_items.append(item)

    db.session.add(poki_popular)
    db.session.add(poki_bowls)
    db.session.add(poki_humphry)
    db.session.add(poki_leeuwen)
    db.session.add(poki_drinks)


    # Tony's Pizza Napoletana
    tony = Restaurant.query.get(4)
    tony_items = Item.query.filter(Item.restaurant_id == tony.id).all()

    tony_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=4)
    tony_sides = Menu(name="Sides", description="Vegetarian", restaurant_id=4)
    tony_pasta = Menu(name="Housemade Pasta", restaurant_id=4)
    tony_american = Menu(name="Classic American Pizza", restaurant_id=4)
    tony_italian = Menu(name="Classic Italian Pizza", restaurant_id=4)
    tony_new_york = Menu(name="20\" New York", restaurant_id=4)
    tony_wines = Menu(name="Wines", restaurant_id=4)

    for item in tony_items:
        item_id = item.id
        if item_id >= 71 and item_id <= 76: tony_popular.menu_items.append(item)
        if item_id == 77 or item_id == 75: tony_sides.menu_items.append(item)
        if item_id == 78 or item_id == 79: tony_pasta.menu_items.append(item)
        if (item_id >= 80 and item_id <= 83) or item_id == 72: tony_american.menu_items.append(item)
        if item_id == 84 or item_id == 85: tony_italian.menu_items.append(item)
        if item_id == 86 or item_id == 87 or item_id == 73: tony_new_york.menu_items.append(item)
        if item_id >= 88 and item_id <= 91: tony_wines.menu_items.append(item)

    db.session.add(tony_popular)
    db.session.add(tony_sides)
    db.session.add(tony_pasta)
    db.session.add(tony_american)
    db.session.add(tony_italian)
    db.session.add(tony_new_york)
    db.session.add(tony_wines)

    # KFC
    kfc = Restaurant.query.get(5)
    kfc_items = Item.query.filter(Item.restaurant_id == kfc.id).all()

    kfc_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=5)
    kfc_bucket = Menu(name="Bucket Meals", restaurant_id=5)
    kfc_wings = Menu(name="Kentucky Fried Wings", restaurant_id=5)
    kfc_sides = Menu(name="Sides", restaurant_id=5)
    kfc_alc = Menu(name="A La Carte", restaurant_id=5)
    kfc_beverages = Menu(name="Beverages", restaurant_id=5)

    for item in kfc_items:
        item_id = item.id
        if item_id >= 92 and item_id <= 95: kfc_popular.menu_items.append(item)
        if item_id >= 96 and item_id <= 98: kfc_bucket.menu_items.append(item)
        if item_id >= 99 and item_id <= 101: kfc_wings.menu_items.append(item)
        if item_id >= 102 and item_id <= 106: kfc_sides.menu_items.append(item)
        if item_id >= 107 and item_id <= 110: kfc_alc.menu_items.append(item)
        if (item_id >= 111 and item_id <= 112) or item_id == 95: kfc_beverages.menu_items.append(item)
        

    db.session.add(kfc_popular)
    db.session.add(kfc_bucket)
    db.session.add(kfc_wings)
    db.session.add(kfc_sides)
    db.session.add(kfc_alc)
    db.session.add(kfc_beverages)


    # Honey Honey
    honey = Restaurant.query.get(6)
    honey_items = Item.query.filter(Item.restaurant_id == honey.id).all()

    honey_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=6)
    honey_breakfast = Menu(name="Breakfast Specials", restaurant_id=6)
    honey_eggs = Menu(name="Eggs & Omelettes", restaurant_id=6)
    honey_savory = Menu(name="Savory Crepes", restaurant_id=6)
    honey_desserts = Menu(name="Desserts", restaurant_id=6)
    honey_sandwiches = Menu(name="Sandwiches", restaurant_id=6)
    honey_soups_salads = Menu(name="Soups & Salads", restaurant_id=6)
    honey_pasta = Menu(name="Pastas & Entrees", restaurant_id=6)

    for item in honey_items:
        item_id = item.id
        if item_id >= 113 and item_id <= 117: honey_popular.menu_items.append(item)
        if item_id >= 114 and item_id <= 119: honey_breakfast.menu_items.append(item)
        if item_id >= 120 and item_id <= 123: honey_eggs.menu_items.append(item)
        if item_id >= 124 and item_id <= 128: honey_savory.menu_items.append(item)
        if item_id >= 129 and item_id <= 130: honey_desserts.menu_items.append(item)
        if item_id >= 131 and item_id <= 134: honey_sandwiches.menu_items.append(item)
        if item_id >= 135 and item_id <= 137: honey_soups_salads.menu_items.append(item)
        if item_id >= 138 and item_id <= 140: honey_pasta.menu_items.append(item)

    db.session.add(honey_popular)
    db.session.add(honey_breakfast)
    db.session.add(honey_eggs)
    db.session.add(honey_savory)
    db.session.add(honey_desserts)
    db.session.add(honey_sandwiches)
    db.session.add(honey_soups_salads)
    db.session.add(honey_pasta)


    # Smash Burger
    smash = Restaurant.query.get(7)
    smash_items = Item.query.filter(Item.restaurant_id == smash.id).all()

    smash_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=7)
    smash_burgers = Menu(name="Burgers | 100% Certified Angus Beef", restaurant_id=7)
    smash_turkey = Menu(name="Turkey Burgers", restaurant_id=7)
    smash_sides = Menu(name="Fries and Sides", restaurant_id=7)
    smash_shakes = Menu(name="Milkshakes", restaurant_id=7)
    
    for item in smash_items:
        item_id = item.id
        if item_id >= 141 and item_id <= 146: smash_popular.menu_items.append(item)
        if (item_id >= 147 and item_id <= 150) or (item_id >= 141 and item_id <= 143): smash_burgers.menu_items.append(item)
        if item_id >= 151 and item_id <= 154: smash_turkey.menu_items.append(item)
        if (item_id >= 155 and item_id <= 156) or (item_id >= 144 and item_id <= 146): smash_sides.menu_items.append(item)
        if item_id >= 157 and item_id <= 161: smash_shakes.menu_items.append(item)
        
    db.session.add(smash_popular)
    db.session.add(smash_burgers)
    db.session.add(smash_turkey)
    db.session.add(smash_sides)
    db.session.add(smash_shakes)


    # Subway
    subway = Restaurant.query.get(8)
    subway_items = Item.query.filter(Item.restaurant_id == subway.id).all()

    subway_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=8)
    subway_all_sandwiches = Menu(name="All Sandwiches", restaurant_id=8)
    subway_salads = Menu(name="Salads", restaurant_id=8)
    subway_sides = Menu(name="Sides", restaurant_id=8)
    subway_drinks = Menu(name="Drinks", restaurant_id=8)
    
    for item in subway_items:
        item_id = item.id
        if item_id >= 162 and item_id <= 167: subway_popular.menu_items.append(item)
        if item_id >= 162 and item_id <= 176: subway_all_sandwiches.menu_items.append(item)
        if item_id >= 177 and item_id <= 182: subway_salads.menu_items.append(item)
        if item_id >= 183 and item_id <= 188: subway_sides.menu_items.append(item)
        if item_id >= 189 and item_id <= 192: subway_drinks.menu_items.append(item)
        
    db.session.add(subway_popular)
    db.session.add(subway_all_sandwiches)
    db.session.add(subway_salads)
    db.session.add(subway_sides)
    db.session.add(subway_drinks)


    # Hinodeya
    hinodeya = Restaurant.query.get(9)
    hinodeya_items = Item.query.filter(Item.restaurant_id == hinodeya.id).all()

    hinodeya_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=9)
    hinodeya_ramen = Menu(name="Ramen: Japanese Noodles", restaurant_id=9)
    hinodeya_okazu = Menu(name="Okazu - Side Dish, Japanese", restaurant_id=9)
    hinodeya_otsumami = Menu(name="Otsumami - Small Bites, Japanese", restaurant_id=9)
    hinodeya_beverages = Menu(name="Beverages", restaurant_id=9)

    
    for item in hinodeya_items:
        item_id = item.id
        if item_id >= 193 and item_id <= 201: hinodeya_popular.menu_items.append(item)
        if (item_id >= 193 and item_id <= 195) or (item_id >= 196 and item_id <= 199): hinodeya_ramen.menu_items.append(item)
        if item_id == 195 or item_id == 200 or (item_id >= 202 and item_id <= 205): hinodeya_okazu.menu_items.append(item)
        if item_id == 206 or item_id == 207 or item_id == 201: hinodeya_otsumami.menu_items.append(item)
        if item_id >= 208 and item_id <= 212: hinodeya_beverages.menu_items.append(item)
        
    db.session.add(hinodeya_popular)
    db.session.add(hinodeya_ramen)
    db.session.add(hinodeya_okazu)
    db.session.add(hinodeya_otsumami)
    db.session.add(hinodeya_beverages)


    # Hinodeya
    lers = Restaurant.query.get(10)
    lers_items = Item.query.filter(Item.restaurant_id == lers.id).all()

    lers_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=10)
    lers_appetizers = Menu(name="Appetizers", restaurant_id=10)
    lers_noodles = Menu(name="Pan Fried Noodles", restaurant_id=10)
    lers_curries = Menu(name="Coconut Milk Curries", restaurant_id=10)
    lers_specialties = Menu(name="House Specialties", restaurant_id=10)
    lers_sides = Menu(name="Side Dishes", restaurant_id=10)

    
    for item in lers_items:
        item_id = item.id
        if item_id >= 213 and item_id <= 220: lers_popular.menu_items.append(item)
        if (item_id >= 221 and item_id <= 224) or (item_id >= 216 and item_id <= 217): lers_appetizers.menu_items.append(item)
        if item_id >= 213 and item_id <= 215: lers_noodles.menu_items.append(item)
        if item_id >= 218 and item_id <= 220: lers_curries.menu_items.append(item)
        if item_id >= 225 and item_id <= 231: lers_specialties.menu_items.append(item)
        if item_id >= 232 and item_id <= 237: lers_sides.menu_items.append(item)

    db.session.add(lers_popular)
    db.session.add(lers_appetizers)
    db.session.add(lers_noodles)
    db.session.add(lers_curries)
    db.session.add(lers_specialties)
    db.session.add(lers_sides)


    # Chipotle
    chipotle = Restaurant.query.get(11)
    chipotle_items = Item.query.filter(Item.restaurant_id == chipotle.id).all()

    chipotle_popular = Menu(name="Popular Items", description="The most commonly ordered items and dishes from this store.", restaurant_id=11)
    chipotle_entrees = Menu(name="Entrees", restaurant_id=11)
    chipotle_sides = Menu(name="Sides", restaurant_id=11)
    chipotle_drinks = Menu(name="Drinks", restaurant_id=11)

    
    for item in chipotle_items:
        item_id = item.id
        if item_id >= 238 and item_id <= 244: chipotle_popular.menu_items.append(item)
        if item_id >= 238 and item_id <= 242: chipotle_entrees.menu_items.append(item)
        if (item_id >= 243 and item_id <= 245) or (item_id >= 247 and item_id <= 252): chipotle_sides.menu_items.append(item)
        if (item_id >= 253 and item_id <= 260) or item_id == 246: chipotle_drinks.menu_items.append(item)

    db.session.add(chipotle_popular)
    db.session.add(chipotle_entrees)
    db.session.add(chipotle_sides)
    db.session.add(chipotle_drinks)


    db.session.commit()


def undo_menus():
    db.session.execute('TRUNCATE menus RESTART IDENTITY CASCADE;')
    db.session.commit()
