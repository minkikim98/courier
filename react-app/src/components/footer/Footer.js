import React from 'react';
import { Link } from 'react-router-dom';
import "./Footer.css";

import logo from '../../images/logo.png';

const Footer = () => {
    return (
        <div id="footer">
            <div id="footer-top">
                <Link to="/">
                    <img src={logo} alt="Courier logo."/>
                </Link>
                <Link to="/about" id="footer-about"> 
                    About Us
                </Link>
                <div id="creator-info">
                    <div>
                        Created by Minki Kim
                    </div>
                    <div id="creator-info-links">
                        <Link to="https://www.linkedin.com/in/min-ki-kim-34888a156/">
                            <i className="fab fa-linkedin"></i>
                        </Link>
                        <Link to="https://github.com/minkikim98">
                            <i className="fab fa-github-square"></i>
                        </Link>
                    </div>
                </div>
            </div>
            <div id="disclaimer">This website is not affiliated with or promoted by Doordash or any of its associates, and is purely intended for demonstrative 
                purposes. Content for this site is attributed to doordash, but is not intended to be an accurate representation of Doordash's policies, prices, 
                or text.
            </div>
        </div>
    )
}

export default Footer;