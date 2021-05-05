from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired
from app.models import Cart, Item

def quantityReasonable(form, field):
    print("Checking if payed amount is not zero, negative, or too large", field.data)
    quantity = field.data
    if quantity < 1 or quantity > 100:
        raise ValidationError("Incorrect quantity.")

# def cartExists(form, field):
#     print("Checking if cart exists.", field.data)
#     cart_id = field.data
#     if Cart.query.get(cart_id) is not None:
#         raise ValidationError("Cart does not exist.")

def itemExists(form, field):
    print("Checking if item exists.", field.data)
    item_id = field.data
    if Item.query.get(item_id) is not None:
        raise ValidationError("Item does not exist.")


class AddToCartForm(FlaskForm):
    quantity = IntegerField("quantity", validators=[DataRequired(), quantityReasonable])
    # cart_id = IntegerField("cart_id", validators=[DataRequired(), cartExists])
    item_id = IntegerField("item_id", validators=[DataRequired(), itemExists])
