import React from 'react';

import Footer from '../footer/Footer';

import "./Checkout.css";

const Checkout = () => {
    return (
        <>
            <div className="checkout-body">
                <div className="checkout-main">This is the checkout page.</div>
                <div className="checkout-right">This will be the right sidebar for the checkout page.</div>
            </div>
            <Footer />
        </>
    )
}

export default Checkout;