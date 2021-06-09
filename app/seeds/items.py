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

    # McDonald's

    # Most Popular
    item17 = Item(name="The BTS Meal", description="10 Piece McNugget, Medium Fry, Medium Drink (740 - 980 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/390a4bc8-3630-4ddd-a0a0-1a099851a7aa-retina-large-jpeg")
    db.session.add(item17)

    item18 = Item(name="Big Mac Meal", description="(870 - 1110 Cal.)", price=12.23, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/79ffceed-52b7-45e1-9606-36cd173572ae-retina-large.jpg")
    db.session.add(item18)

    item19 = Item(name="10 Piece McNuggets Meal", description="(740 - 980 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/0a37a43f-4320-419a-a72c-1138e35a73b5-retina-large-jpeg")
    db.session.add(item19)

    item20 = Item(name="40 McNuggets", description="(1660 Cal.)", price=11.59, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/8614e107-dabd-4218-be57-6df8fd619a3e-retina-large-jpeg")
    db.session.add(item20)

    item21 = Item(name="French Fries", description="(220 Cal.)", price=2.79, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/d0d5bdfb-a107-4050-8323-5bc4ad603adf-retina-large.jpg")
    db.session.add(item21)

    item22 = Item(name="Oreo McFlurry", description="(340 Cal.)", price=3.49, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e7bb4627-110a-45f4-ba67-96e78a54959c-retina-large.jpg")
    db.session.add(item22)

    # Combo Meals
    item23 = Item(name="Spicy Chicken Sandwich Meal", description="(850 - 1090 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/1ee067c2-e907-4516-bbec-b555b11d3ffe-retina-large-jpeg")
    db.session.add(item23)

    item24 = Item(name="Quarter Pounder with Cheese Meal", description="(840 - 1080 Cal.)", price=12.53, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/804feda6-e466-4c58-b8b4-aab1718979c7-retina-large.jpg")
    db.session.add(item24)

    item25 = Item(name="2 Cheeseburger Meal", description="(920 - 1160 Cal.)", price=9.62, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7015a61f-6179-4349-9087-82bb1d641a2b-retina-large-jpeg")
    db.session.add(item25)

    item26 = Item(name="Filet O Fish Meal", description="(700 - 940 Cal.)", price=11.43, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4f6307a5-9392-4da1-9861-96686d136529-retina-large-jpeg")
    db.session.add(item26)

    # Happy Meals
    item27 = Item(name="Hamburger - Happy Meal", description="(375 Cal.)", price=4.69, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/45699277-6544-4ffc-8931-f86de29d8ff6-retina-large-jpeg")
    db.session.add(item27)

    item28 = Item(name="Cheese Burger - Happy Meal", description="(430 - 590 Cal.)", price=4.99, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f33ae198-98e2-4e73-b7f8-a64ca856e377-retina-large.jpg")
    db.session.add(item28)

    item29 = Item(name="6pc Chicken McNuggets Happy Meal", description="(430 - 530 Cal.)", price=6.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/b912085a-31bf-4bf1-9e42-e4897acda5f2-retina-large-jpeg")
    db.session.add(item29)

    # McCafe
    item30 = Item(name="Premium Roast Coffee", description="(0 Cal.)", price=1, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/a7e0c926-9110-427c-8662-13ba8e86459e-retina-large.jpg")
    db.session.add(item30)
    
    item31 = Item(name="Decaf Coffee", description="(0 Cal.)", price=1, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/a7e0c926-9110-427c-8662-13ba8e86459e-retina-large.jpg")
    db.session.add(item31)
    
    item32 = Item(name="Hot Tea", description="(10 Cal.)", price=1.59, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c2d0fc5c-7ce1-4157-9267-6f630b09e9bb-retina-large.jpg")
    db.session.add(item32)
    
    item33 = Item(name="Iced Coffee", description="(140 Cal.)", price=2.33, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/0a59dc23-88bd-4fff-8f2c-8b7f00b7b713-retina-large.jpg")
    db.session.add(item33)
    
    item34 = Item(name="Premium Hot Chocolate", description="(380 Cal.)", price=2.50, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/41adc628-bd31-4385-b44a-42a3b4a779de-retina-large.jpg")
    db.session.add(item34)
    
    item35 = Item(name="Mocha Frappé", description="(420 Cal.)", price=2.63, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/78476d12-1e2a-41fc-a0d4-4dccca626bd9-retina-large.jpg")
    db.session.add(item35)
    
    item36 = Item(name="Caramel Macchiato", description="(270 Cal.)", price=2.50, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7f3df6f7-53d1-4413-a9a1-d02dd854c160-retina-large-jpeg")
    db.session.add(item36)
    
    item37 = Item(name="Americano", description="(5 Cal.)", price=2.50, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6dcdd42a-a4e1-457f-a665-e66eae424b1e-retina-large-jpeg")
    db.session.add(item37)
    
    # Fries, Sides, and More
    item38 = Item(name="Apple Slices", description="(15 Cal.)", price=1.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/11616027-10b3-4d12-aab9-ea9f86666240-retina-large-jpeg")
    db.session.add(item38)

    # Sweets & Treats
    item39 = Item(name="Chocolate Shake", description="(520 Cal.)", price=3.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/95cbd3c9-6656-4fd2-af8c-8a5562ebb207-retina-large-jpeg")
    db.session.add(item39)
    
    item40 = Item(name="Strawberry Shake", description="(530 Cal.)", price=3.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/96ee505d-8f1b-4bc7-b9ad-aefc5fb151c1-retina-large-jpeg")
    db.session.add(item40)
    
    item41 = Item(name="M&M McFlurry", description="(420 Cal.)", price=3.49, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/09bb4bc1-c5fc-4a99-b3b4-445a7c1d33b5-retina-large-jpeg")
    db.session.add(item41)
    
    item42 = Item(name="Apple Pie", description="(230 Cal.)", price=1.79, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/58dc5072-93cd-42aa-8221-0d65c7f6d019-retina-large-jpeg")
    db.session.add(item42)
    
    # Beverages
    item43 = Item(name="Coke®", description="(150 Cal.)", price=1.39, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/150c813d-ea57-48cc-a6eb-e11d76dc8e57-retina-large.jpg")
    db.session.add(item43)
    
    item44 = Item(name="Diet Coke®", description="(0 Cal.)", price=1.25, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4ed2e4b1-1b34-48db-b545-a9d1aa9d1764-retina-large.jpg")
    db.session.add(item44)
    
    item45 = Item(name="Dr Pepper®", description="(140 Cal.)", price=1.39, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/8de9f60f-2c6c-42cb-b169-2a07970a82a4-retina-large.jpg")
    db.session.add(item45)
    
    item46 = Item(name="Minute Maid® Orange Juice", description="(150 Cal.)", price=3.39, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/b2377684-b570-4b46-864a-4dab1b13be42-retina-large-jpeg")
    db.session.add(item46)
    
    item47 = Item(name="Dasani® Bottled Water", description="(0 Cal.)", price=2.59, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/31ba6fe2-51f9-4b66-aeef-4a86a21c7b00-retina-large-jpeg")
    db.session.add(item47)
    
    item48 = Item(name="Milk", description="(120 Cal.)", price=2.09, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/88c5903e-10d7-4d26-864c-008384fae497-retina-large-jpeg")
    db.session.add(item48)
    
    item49 = Item(name="Sweet Iced Tea", description="(170 Cal.)", price=1.25, restaurant_id=2,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/ff74f476-f8a4-4e0f-a9f4-9a635b4c156f-retina-large-jpeg")
    db.session.add(item49)
    

    # Poki Time

    # Most Popular
    item50 = Item(name="Spicy Combo Poki Bowl", description="Half ahi tuna and half salmon marinated in our spicy mayo sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/bb85dbf9-fea4-4cac-82d4-642e54169ce6-retina-large.jpg")
    db.session.add(item50)

    item51 = Item(name="Original Combo Poki Bowl", description="Half ahi tuna and half salmon marinated in our original house sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/f4a6bdf0-d61f-496e-b2d1-4fdae17874bc-retina-large.jpg")
    db.session.add(item51)

    item52 = Item(name="Original Salmon Poki Bowl", description="Salmon marinated in our original house sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e51a0e17-a2a2-423c-afb4-99eddabe8f86-retina-large.jpg")
    db.session.add(item52)

    item53 = Item(name="Spicy Salmon Poki Bowl", description="Salmon marinated in our spicy mayo sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/c493b7a6-c4c9-43a6-b12a-e439111dd5c3-retina-large.jpg")
    db.session.add(item53)

    item54 = Item(name="Poki Bowl and Drink Combo", description="Your choice of poki bowl with your choice of drink! We cannot make substitutions.", price=17.75, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6c7f429f-5610-4ead-ad42-7c064a4e7112-retina-large.jpg")
    db.session.add(item54)

    item55 = Item(name="Poki Meal Combo", description="Make it a full meal with your choice of poki bowl, drink, and ice cream pint! We cannot make substitutions.", price=26.49, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/6914cd0a-50a2-4e4e-8a60-3e236293333b-retina-large.jpg")
    db.session.add(item55)

    # Poki Bowls
    item56 = Item(name="Original Ahi Tuna Poki Bowl", description="Ahi tuna marinated in our original house sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/60d3d15b-47e6-4e08-982f-62047c3f8cd1-retina-large.jpg")
    db.session.add(item56)

    item57 = Item(name="Spicy Ahi Tuna Poki Bowl", description="Ahi tuna marinated in our spicy mayo sauce, alongside dashi-infused sushi rice, seaweed salad, and kimchi. Furikake, green onions, and red onions included for seasoning. Contains gluten, dairy, soy, and nightshades. We cannot make substitutions.", price=15.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/70723679-bcfa-45c5-93d5-e2984d9a3dc6-retina-large.jpg")
    db.session.add(item57)

    # Humphry Slocombe Ice Cream
    item58 = Item(name="Black Sesame", description="Toasted black sesame seeds with sesame oil added for extra oomph. There’s no going back. Gluten-free. Contains dairy, eggs, and sesame seeds. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/7ae0bf79-add6-490e-b3de-84f15a75d198-retina-large.jpg")
    db.session.add(item58)

    item59 = Item(name="Hong Kong Milk Tea", description="Black tea ice cream made with housemade almond cookies. Made in partnership with Chef Melissa King. Contains gluten, eggs, dairy, and almonds. We cannot make substitutions.", price=10, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/1b75894c-15f7-4f2d-92ed-02a93b3c6e6a-retina-large.jpg")
    db.session.add(item59)

    item60 = Item(name="Matchadoodle", description="Housemade snickerdoodle cookies and the best green tea from Kyoto come together for an incredible flavor combination. Contains gluten, eggs, and dairy. We cannot make substitutions.", price=10, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/43293ab4-0a42-4e44-8128-babbadc9909a-retina-large.jpg")
    db.session.add(item60)

    item61 = Item(name="Secret Breakfast", description="Bourbon ice cream with housemade Cornflake cookies. Contains more than 0.5% of alcohol, as well as gluten, dairy, and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e1b61246-31dd-4147-bc96-9cbe35ca74b0-retina-large.jpg")
    db.session.add(item61)

    item62 = Item(name="Honey Graham", description="Raw blackberry honey ice cream with house-made graham crackers folded in. Contains gluten, dairy, and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/ee883cc6-08cf-4080-a010-7fdc4fec8e79-retina-large.jpg")
    db.session.add(item62)

    # Van Leeuwen Ice Cream
    item63 = Item(name="Honeycomb", description="Nothing makes us happier than this Honeycomb Ice Cream. Despite being called honeycomb, it's not made from any honey at all. It’s made with housemade caramel candy. That all might seem confusing until you realize that ice cream is also made without ice. Your whole life has been a lie. Contains tree nuts, dairy, and eggs. We cannot make substitutions.", price=10, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e5125ff8-9a89-41f1-859d-ab2af1b97939-retina-large.jpg")
    db.session.add(item63)

    item64 = Item(name="Mint Chip", description="Nothing makes us happier than this Mint Chip Ice Cream. We use single origin chocolate chips, so you can taste their true flavor profile. We add in a little pure peppermint extract and <chef’s kiss>. Contains dairy and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/9be10c05-a416-458f-9e92-9f64282efcc6-retina-large.jpg")
    db.session.add(item64)

    item65 = Item(name="Strawberry", description="Nothing makes us happier than this Strawberry Ice Cream. Oregon-grown strawberries. Delicately picked at peak ripeness. Then shoved in to a dark alley where fresh cream, egg yolks, and pure cane sugar get to work initiating strawberries in to the ice cream gang. Contains dairy and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/23a4583d-35c1-4132-853f-c3a8c41ea989-retina-large.jpg")
    db.session.add(item65)

    item66 = Item(name="Cookies and Cream", description="Nothing makes us happier than this Cookies & Cream Ice Cream. Nothing. Not children. Not dogs. Not rainbows. Nothing. Dark chocolate chip cookies + a rich cream filling + cold-ground vanilla bean ice cream = non-child, non-dog, non-rainbow happiness. Contains gluten, tree nuts, dairy, and eggs. We cannot make substitutions.", price=10.00, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/e287bb57-28d4-471f-a5ba-c2278685404a-retina-large.jpg")
    db.session.add(item66)

    # Drinks
    item67 = Item(name="Topo Chico Mineral Water", description="12 oz glass bottle of sparkling mineral water. Bottled at the source in Monterrey, Mexico since 1895 with a natural mineral composition perfect for quenching thirst!", price=3.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/d1908724-cbea-4171-b31d-f776f3accb9d-retina-large.jpg")
    db.session.add(item67)

    item68 = Item(name="Mexican Coke", description="12 oz glass bottle of Coke, sweetened with real cane sugar.", price=3.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/84726d84-d3a1-484c-bd86-3ffb67997a3a-retina-large.jpg")
    db.session.add(item68)

    item69 = Item(name="La Colombe Coffee Draft Latte", description="9 oz can. Experience the full taste and texture of a true cold latte, complete with a frothy layer of silky foam. Made with real ingredients like nutrient-rich and lactose-free milk and two shots of espresso.", price=5.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/4a3b903e-1ba7-4801-95b1-a3659192dc24-retina-large.jpg")
    db.session.add(item69)

    item70 = Item(name="Dasani", description="16.9 oz bottle of Dasani's premium tasting, pure, and delicious water.", price=2.99, restaurant_id=3,
        image_url="https://img.cdn4dd.com/cdn-cgi/image/fit=contain,width=300,format=auto,quality=50/https://cdn.doordash.com/media/photos/34407095-a71c-4780-8dd2-556cd4711fc4-retina-large.jpg")
    db.session.add(item70)


    db.session.commit()


    # item = Item(name="", description="", price=, restaurant_id=3,
    #     image_url="")
    # db.session.add(item)

def undo_items():
    db.session.execute('TRUNCATE items RESTART IDENTITY CASCADE;')
    db.session.commit()
