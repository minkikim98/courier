import React from "react";
import { Link } from 'react-router-dom';

import "./Intro.css";

// import Logo from "../../images/logo.png"

const IntroPage = () => {
    return (
        <div>
            <img className="intro__hero-img" src="https://www.teahub.io/photos/full/38-388348_bicycle-wallpaper-hd.jpg" alt="Banner"></img>
            <div className="intro">
                <div className="intro__banner-text">Welcome to Courier</div>
                <div className="intro__caption">No gas. No fumes. Just fresh food pedaled straight to your doorstep.</div>
                <div className="intro__description">Here at Courier, we don't belive that we have to sacrifice speed to make good time. We're committed 
                    to an eco-friendly and sustainable model that's good for the environment, and for you! All of our delivery services are provided 
                    strictly through pedal-power. Now you can enjoy fresh food from all of your favorite local restaurants, and help keep the earth green. 
                    That's a win-win in our book.
                </div>
                <Link to="/" className="homepage-link">Ready to order?</Link>
            </div>
        </div>
    )
}

export default IntroPage;