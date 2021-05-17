from flask.cli import AppGroup
from .users import seed_users, undo_users
from .cuisines import seed_cuisines, undo_cuisines
from .restaurants import seed_restaurants, undo_restaurants
from .menus import seed_menus, undo_menus
from .items import seed_items, undo_items
from .carts import seed_carts, undo_carts
from .cart_items import seed_cart_items, undo_cart_items

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_cuisines()
    seed_restaurants()
    seed_carts()
    seed_items()
    seed_menus()
    seed_cart_items()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_cart_items()
    undo_carts()
    undo_cuisines()
    undo_restaurants()
    undo_items()
    undo_menus()
