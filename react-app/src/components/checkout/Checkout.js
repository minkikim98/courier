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
                        <div>Your Delivery Details</div>
                        <div className="checkout-row">
                            <div className="checkout-row__label">TIME</div>
                            <div className="checkout-row__main"></div>
                        </div>
                        <div className="checkout-row">
                            <div className="checkout-row__label">ADDRESS</div>
                            <div className="checkout-row__main"></div>
                        </div>
                        <div className="checkout-row">
                            <div className="checkout-row__label">CONTACT</div>
                            <div className="checkout-row__main"></div>
                        </div>
                        <div className="checkout-row">
                            <div className="checkout-row__label">PAYMENT</div>
                            <div className="checkout-row__main"></div>
                        </div>
                        <div className="checkout-row">
                            <div className="checkout-row__label">SUMMARY</div>
                            <div className="checkout-row__main"></div>
                        </div>
                    </div>
                </div>
                <div className="checkout-right">This will be the right sidebar for the checkout page.</div>
            </div>
            <Footer />
        </>
    )
}

export default Checkout;