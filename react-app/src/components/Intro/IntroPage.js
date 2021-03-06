import React from "react";
import { Link } from 'react-router-dom';

import Footer from '../footer/Footer';
import SimpleNavBar from '../navbar/SimpleNavBar';

import "./Intro.css";

import introBanner from '../../images/intro-image.jpeg';
import headshot from '../../images/headshot.jpeg';

const IntroPage = () => {
    return (
        <>
            <SimpleNavBar />
            <div className="intro">
                <div id="intro-top">
                    <div id="intro-info">
                        <div className="intro__banner-text">Welcome to <span id="description-courier">Courier</span></div>
                        <div className="intro__caption">No gas. No fumes. Just fresh food pedaled straight to your doorstep.</div>
                        <div className="intro__description">Here at Courier, we don't belive that we have to sacrifice speed to make good time. We're committed 
                            to an eco-friendly and sustainable model that's good for the environment, and for you! All of our delivery services are provided 
                            strictly through pedal-power. Now you can enjoy fresh food from all of your favorite local restaurants, and help keep the earth green. 
                            That's a win-win in our book.
                        </div>
                        <div className="homepage-link">
                            <Link to="/">
                                Ready to order? 
                                <i className="far fa-arrow-alt-circle-right"></i>
                            </Link>
                        </div>
                    </div>
                    <img src={introBanner} alt="Vector art of a man riding a bicycle."></img>
                </div>
                <div id="intro-creator">
                    <div id="intro-creator__info">
                        <div id="intro-creator__info-heading">
                            <div>Meet the creator:</div>
                            <img src={headshot} alt="A headshot of a very good-looking man."></img>
                        </div>
                        <div id="intro-creator__info-text">Hi! My name is Minki. It's nice to meet you. I'm an aspiring software developer with experience in Javascript, Python, Flask, React, and more! 
                            If you want to see more of my projects or want to contact me, feel free to follow up with me on Github or LinkedIn!
                        </div>
                    </div>
                </div>
                <Footer />
            </div>
        </>
    )
}

export default IntroPage;