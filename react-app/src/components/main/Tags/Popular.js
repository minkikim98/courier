import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

import RestaurantLink from "./RestaurantLink";

import "./Tags.css"

const Popular = () => {
    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const popularRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.tags.some(tag => tag.tag_name === "Popular"));

    return (
        <div className="tag-container">
            <div className="tag__left">
                <div className="tag__label">Popular Restaurants in SF</div>
                <div className="tag__view-all">
                    <div>See All</div>
                    <i className="fas fa-arrow-right"></i>
                </div>
            </div>
            {popularRestaurants.length && <div className="tagged-restaurants">
                <div className="tagged-restaurants__top">
                    <RestaurantLink restaurant={popularRestaurants[0]} column="top"/>
                    <RestaurantLink restaurant={popularRestaurants[1]} column="top"/>
                </div>
                <div className="tagged-restaurants__bottom">
                    <RestaurantLink restaurant={popularRestaurants[2]} column="bottom"/>
                    <RestaurantLink restaurant={popularRestaurants[3]} column="bottom"/>
                    <RestaurantLink restaurant={popularRestaurants[4]} column="bottom"/>
                </div>
                
                {/* {allRestaurants && popularRestaurants.map(restaurant => (
                    <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className="tagged-restaurant">
                        <img src={restaurant.image_url} alt={restaurant.name}></img>
                        <div className="tagged-restaurant__name">{restaurant.name}</div>
                        <div className="tagged-restaurant__address">{restaurant.address}</div>
                    </Link>
                ))} */}
            </div>}
        </div>
    )
}

export default Popular;