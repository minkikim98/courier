import React, { useState, useEffect } from 'react';
import Cart from "./Cart"

const ShowCartButton = () => {
    const [showCart, setShowCart] = useState(false);

    const openCart = () => {
        if (showCart) return;
        setShowCart(true);
    };

    useEffect(() => {
        if (!showCart) return;

        const closeCart = () => {
            setShowCart(false);
        };

        // document.addEventListener('submit', closeEditDateTime);
        document.getElementById("close-cart").addEventListener('click', closeCart);
    }, [showCart]);

    return (
        <>
            <button id="cart"
                onClick={openCart}>
                Cart
            </button>
            {showCart && <Cart />}
        </>
    )
}

export default ShowCartButton;
