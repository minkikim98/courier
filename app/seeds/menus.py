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

    poki_popular = Menu(name='Most Popular', restaurant_id=3)
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


    db.session.commit()


def undo_menus():
    db.session.execute('TRUNCATE menus RESTART IDENTITY CASCADE;')
    db.session.commit()
