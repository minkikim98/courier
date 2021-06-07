import React from 'react';
import { Link } from 'react-router-dom';

import logo from "../../images/logo.png";

import "./Navbar.css"

const SimpleNavBar = () => {
    return (
        <div className="simple-navbar">
            <img src={logo} alt="Courier Logo"></img>
            <Link to="/" className="navbar-center-item">
                COURIER
            </Link>
        </div>
    )
}

export default SimpleNavBar;