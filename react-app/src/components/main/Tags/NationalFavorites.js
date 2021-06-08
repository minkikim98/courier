import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import RestaurantLink from "./RestaurantLink";

import "./Tags.css"

const NationalFavorites = () => {
    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const nationalFavoriteRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.tags.some(tag => tag.tag_name === "National Favorites"));

    return (
        <div className="tag-container">
            <div className="tag__left">
                <div className="tag__label">National Favorites</div>
                <Link to="/tags/2" className="tag__view-all">
                    <div>See All</div>
                    <i className="fas fa-arrow-right"></i>
                </Link>
            </div>
            <div className="tagged-restaurants">
                <div className="tagged-restaurants__top">
                    <RestaurantLink restaurant={nationalFavoriteRestaurants[2]} column="top" />
                    <RestaurantLink restaurant={nationalFavoriteRestaurants[3]} column="top" />
                </div>
                <div className="tagged-restaurants__bottom">
                    <RestaurantLink restaurant={nationalFavoriteRestaurants[1]} column="bottom" />
                    <RestaurantLink restaurant={nationalFavoriteRestaurants[0]} column="bottom" />
                    <RestaurantLink restaurant={nationalFavoriteRestaurants[4]} column="bottom" />
                </div>
            </div>
        </div>
    )
}

export default NationalFavorites;