import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';

import { getCart } from "../../store/cart";

import "./Cart.css"

const Cart = () => {
    const dispatch = useDispatch();
    const cartInfo = useSelector(state => state.cart);
    const [errors, setErrors] = useState([]);

    let cartContent;
    const getCartItems = async (e) => {
        const data = await dispatch(getCart());
        console.log(data);
        if (data.errors) setErrors(data.errors);
    }

    useEffect(() => {
        if (!Object.values(cartInfo).length) getCartItems();
        console.log("test")
    })
    
    // useEffect(() => {
    //     if (cartInfo.errors) cartContent = (<div>You are not logged in. Please log in to add items to your cart.</div>)
    //     else cartContent = (<div>You are logged in.</div>)
    // }, [cartInfo])

    return (
        <div className="cart">
            <div id="close-cart">
                <i className="fas fa-times"></i>
            </div>
            <div>
                {errors.map((error) => (
                    <div>{error}</div>
                ))}
            </div>
            <div>
                {cartInfo && <div>
                    <div>For user with ID: {cartInfo.user_id}</div>
                    <div>Corresponds with restaurant ID: {cartInfo.restaurant_id}</div>
                    {cartInfo.cart_items && cartInfo.cart_items.map(cartItem => (
                        <div key={cartItem.id}>
                            <div>Item with ID: {cartItem.id}</div>
                            <div>Quantity: {cartItem.quantity}</div>

                        </div>
                    ))}
                </div>}
            </div>
        </div>
    )
}

export default Cart;