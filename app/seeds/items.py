from app.models import db, Item


def seed_items():
    # Panda Express
    # Popular Items
    item1 = Item(name='Plate', description="Any 1 Side & 2 Entrees", price=10.45, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/c7705748-8e07-46c8-a153-1b7ff0355b75-retina-large-jpeg")
    db.session.add(item1)

    item2 = Item(name='Bigger Plate', description="Any 1 Side & 3 Entrees", price=12.25, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/1c55af2e-adeb-4d4a-8025-0a498eb70a0e-retina-large-jpeg")
    db.session.add(item2)

    item3 = Item(name='Bowl', description="Any 1 Side & 1 Entree", price=8.65, restaurant_id=1, 
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/7eaaa60a-bee5-4216-b192-c306066750c5-retina-large-jpeg")
    db.session.add(item3)

    item4 = Item(name='Kid\'s Meal', description="Any 1 Side & 1 Entree", price=7.70, restaurant_id=1)
    db.session.add(item4)

    item5 = Item(name="Family Meal", description="Any 2 Large Sides & 3 Large Entrees", price=34.80, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/6e737e50-8081-43d1-afe7-15997338bf51-retina-large-jpeg")
    db.session.add(item5)

    # A La Carte
    item6 = Item(name="Wok Seared Steak & Shrimp", price=12.50, restaurant_id=1, 
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/d09f8f91-4411-4ae7-b16d-dab4b02eaaf4-retina-large-jpeg")
    db.session.add(item6)

    item7 = Item(name="Black Pepper Angus Steak", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/905b2a5c-bf3a-414c-b0e7-f541dc781bcf-retina-large-jpeg")
    db.session.add(item7)

    item8 = Item(name="The Original Orange Chicken", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/79213bf5-59f5-48a3-8eed-e91ffaf3a81a-retina-large-jpeg")
    db.session.add(item8)

    item9 = Item(name="Grilled Teriyaki Chicken", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/07c22acc-3036-4030-b003-0000e3e0f53c-retina-large-jpeg")
    db.session.add(item9)

    item10 = Item(name="Honey Walnut Shrimp", price=12.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/a3b14174-a398-4aec-8b76-55124467324e-retina-large.jpg")
    db.session.add(item10)

    # Appetizers
    item11 = Item(name="Chicken Egg Roll", price=6.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/49d374aa-1718-4741-8ccd-afb8095a45cd-retina-large-jpeg")
    db.session.add(item11)

    item12 = Item(name="Veggie Spring Roll", price=5.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/896291aa-ee01-42dd-b8b4-aae584d96ca8-retina-large-jpeg")
    db.session.add(item12)

    # Drinks
    item13 = Item(name="Coca Cola", price=3.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/7fd1126b-54e9-4a69-8a7f-a08b8cc50e64-retina-large-jpeg")
    db.session.add(item13)

    item14 = Item(name="Diet Coke", price=3.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/4a3dd119-acf6-4d02-bb49-c858d920cee2-retina-large-jpeg")
    db.session.add(item14)

    item15 = Item(name="Sprite", price=3.50, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/aa366484-f518-4edc-a281-7699e0a08043-retina-large-jpeg")
    db.session.add(item15)

    item16 = Item(name="Diet Coke", description="16oz Bottle", price=3.00, restaurant_id=1,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=cover,width=150,height=150,format=jpeg,quality=50/https://doordash-static.s3.amazonaws.com/media/photos/4174683f-112d-40da-97af-7c54df019999-retina-large-jpeg")
    db.session.add(item16)


    db.session.commit()


def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
