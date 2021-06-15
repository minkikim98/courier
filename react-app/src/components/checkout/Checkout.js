import React from 'react';

import SimpleNavBar from "../navbar/SimpleNavBar";
import Footer from '../footer/Footer';

import "./Checkout.css";

const Checkout = () => {
    return (
        <>
            <SimpleNavBar />
            <div className="checkout-body">
                <div className="checkout-main__container">
                    <div className="checkout-main">
                        <div className="checkout-row">Your Delivery Details</div>
                        <div>Time</div>
                        <div>Address</div>
                        <div>Contact</div>
                        <div>Payment</div>
                        <div>Summary</div>
                    </div>
                </div>
                <div className="checkout-right">This will be the right sidebar for the checkout page.</div>
            </div>
            <Footer />
        </>
    )
}

export default Checkout;