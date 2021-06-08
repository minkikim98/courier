import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import RestaurantLink from "./RestaurantLink";

import "./Tags.css"

const Cultural = () => {
    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const culturalRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.tags.some(tag => tag.tag_name === "Cultural Cuisine"));

    const cuisine_filter_id = useSelector(state => state.restaurants.cuisine_filter_id);

    return (
        <div className="tag-container">
            <div className="tag__left">
                <div className="tag__label">Cultural Cuisine</div>
                <Link to="/tags/4" className="tag__view-all">
                    <div>See All</div>
                    <i className="fas fa-arrow-right"></i>
                </Link>
            </div>
            {(culturalRestaurants.length && cuisine_filter_id === 0) && <div className="tagged-restaurants">
                <div className="tagged-restaurants__top">
                    <RestaurantLink restaurant={culturalRestaurants[2]} column="top" />
                    <RestaurantLink restaurant={culturalRestaurants[3]} column="top" />
                </div>
                <div className="tagged-restaurants__bottom">
                    <RestaurantLink restaurant={culturalRestaurants[1]} column="bottom" />
                    <RestaurantLink restaurant={culturalRestaurants[0]} column="bottom" />
                    <RestaurantLink restaurant={culturalRestaurants[4]} column="bottom" />
                </div>
            </div>}
        </div>
    )
}

export default Cultural;