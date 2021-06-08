import React from 'react';
import { Link } from 'react-router-dom';

import logo from "../../images/logo.png";

import "./Navbar.css"

const SimpleNavBar = () => {
    return (
        <div className="simple-navbar">
            <Link to="/" className="navbar-center-item">
                <img src={logo} alt="Courier Logo"></img>
                <div>COURIER</div>
            </Link>
        </div>
    )
}

export default SimpleNavBar;