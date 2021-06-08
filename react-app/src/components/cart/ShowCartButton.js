import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { showCart, hideCart } from '../../store/cart';

import Cart from "./Cart"

const ShowCartButton = () => {
    const dispatch = useDispatch();
    const cartVisible = useSelector(state => state.cart.showCart)

    const openCart = () => {
        if (cartVisible) return;
        dispatch(showCart());
    }

    const closeCart = () => {
        if (!cartVisible) return;
        dispatch(hideCart());
    }

    useEffect(() => {
        if (!cartVisible) return;
        document.getElementById("close-cart").addEventListener('click', closeCart);
    })

    return (
        <>
            <button id="cart-button"
                onClick={openCart}>
                <i className="fas fa-shopping-cart"></i>
            </button>
            {cartVisible && <Cart />}
        </>
    )
}

export default ShowCartButton;
