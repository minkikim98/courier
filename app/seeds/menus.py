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
        if item_id == 84 or item_id == 85 or item_id == 73: tony_new_york.menu_items.append(item)
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


    db.session.commit()


def undo_menus():
    db.session.execute('TRUNCATE menus RESTART IDENTITY CASCADE;')
    db.session.commit()
