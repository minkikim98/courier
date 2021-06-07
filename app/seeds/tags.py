from app.models import db, Tag

def seed_tags():
    popular = Tag(name="Popular")
    db.session.add(popular)

    national_favorites = Tag(name="National Favorites")
    db.session.add(national_favorites)

    lunch = Tag(name="Great for Lunch")
    db.session.add(lunch)

    culture = Tag(name="Cultural Cuisine")
    db.session.add(culture)

    db.session.commit()

def undo_tags():
    db.session.execute('TRUNCATE tags RESTART IDENTITY CASCADE;')
    db.session.commit()