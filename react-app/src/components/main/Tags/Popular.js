import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';

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
            <div className="tagged__restaurants">
                {allRestaurants && popularRestaurants.map(restaurant => (
                    <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className="tagged__restaurant">
                        <img src={restaurant.image_url} alt={restaurant.name}></img>
                        <div className="tagged-restaurant__name">{restaurant.name}</div>
                        <div className="tagged-restaurant__address">{restaurant.address}</div>
                    </Link>
                ))}
            </div>
        </div>
    )
}

export default Popular;