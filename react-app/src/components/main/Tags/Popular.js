import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import RestaurantLink from "./RestaurantLink";

import "./Tags.css"

const Popular = () => {
    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const popularRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.tags.some(tag => tag.tag_name === "Popular"));

    return (
        <div className="tag-container">
            <div className="tag__left">
                <div className="tag__label">Popular Restaurants in SF</div>
                <Link to="/tags/1" className="tag__view-all">
                    <div>See All</div>
                    <i className="fas fa-arrow-right"></i>
                </Link>
            </div>
            <div className="tagged-restaurants">
                <div className="tagged-restaurants__top">
                    <RestaurantLink restaurant={popularRestaurants[0]} column="top"/>
                    <RestaurantLink restaurant={popularRestaurants[1]} column="top"/>
                </div>
                <div className="tagged-restaurants__bottom">
                    <RestaurantLink restaurant={popularRestaurants[2]} column="bottom"/>
                    <RestaurantLink restaurant={popularRestaurants[3]} column="bottom"/>
                    <RestaurantLink restaurant={popularRestaurants[4]} column="bottom"/>
                </div>
            </div>
        </div>
    )
}

export default Popular;