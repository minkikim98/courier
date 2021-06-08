import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import RestaurantLink from "./RestaurantLink";

import "./Tags.css"

const Lunch = () => {
    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const lunchRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.tags.some(tag => tag.tag_name === "Great for Lunch"));

    return (
        <div className="tag-container">
            <div className="tag__left">
                <div className="tag__label">Great for Lunch</div>
                <Link to="/tags/3" className="tag__view-all">
                    <div>See All</div>
                    <i className="fas fa-arrow-right"></i>
                </Link>
            </div>
            <div className="tagged-restaurants">
                <div className="tagged-restaurants__top">
                    <RestaurantLink restaurant={lunchRestaurants[2]} column="top" />
                    <RestaurantLink restaurant={lunchRestaurants[3]} column="top" />
                </div>
                <div className="tagged-restaurants__bottom">
                    <RestaurantLink restaurant={lunchRestaurants[1]} column="bottom" />
                    <RestaurantLink restaurant={lunchRestaurants[0]} column="bottom" />
                    <RestaurantLink restaurant={lunchRestaurants[4]} column="bottom" />
                </div>
            </div>
        </div>
    )
}

export default Lunch;