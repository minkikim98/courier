import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getCart } from "../../store/cart";
import { removeFromCart } from "../../store/cart";

import "./Cart.css"

const Cart = () => {
    const dispatch = useDispatch();
    const cartInfo = useSelector(state => state.cart.cart);
    const user = useSelector(state => state.session.user);
    // const [errors, setErrors] = useState([]);

    const getCartItems = async (e) => {
        await dispatch(getCart());
        // if (data.errors) setErrors(data.errors);
    }
    
    const removeFromCartCB = async (itemId) => {
        await dispatch(removeFromCart(itemId));
    }

    useEffect(() => {
        if (!Object.values(cartInfo).length) getCartItems();
    })
    
    let cartContent;

    if (user) {
        if (cartInfo.cart_items && cartInfo.cart_items.length === 0) {
            cartContent = (
                <div className="cart-welcome">Welcome, {user.username}! You currently do not have items in your cart.</div>
            )
        } else {
            cartContent = (
                <div>
                    <div className="cart-welcome">Welcome, {user.username}! Here's your order so far:</div>
                    {cartInfo.cart_items && cartInfo.cart_items.map(cartItem => (
                        <div key={cartItem.id} className="cart__item">
                            <div className="cart__item-name">{cartItem.item_name}</div>
                            {/* <div className="cart__item-quantity">Quantity: {cartItem.quantity}</div> */}
                            <button className="cart__item-delete" onClick={e => removeFromCartCB(cartItem.item_id)}><i className="fas fa-trash"></i></button>
                        </div>
                    ))}
                    <button className="cart__checkout">Checkout</button>
                </div>
            )
        }
    } else {
        cartContent = (<div>You are not logged in. Please log in to add or edit your cart.</div>)
    }
        
    return (
        <div className="cart">
            <div id="close-cart">
                <i className="fas fa-times"></i>
            </div>
            {/* <div>
                {errors.map((error) => (
                    <div>{error}</div>
                ))}
            </div> */}
            <div>
                {cartInfo && cartContent}
            </div>
        </div>
    )
}

export default Cart;