import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllRestaurants } from "../../store/restaurants"
import { Link } from 'react-router-dom';

import "./Popular.css"

const Popular = () => {
    const dispatch = useDispatch();

    const restaurantsToDisplay = useSelector(state => state.restaurants.restaurants) || {};
    const cuisine_filter_id = useSelector(state => state.restaurants.cuisine_filter_id);

    const getAllRestaurantsToDisplay = async (e) => {
        await dispatch(getAllRestaurants());        
    };

    useEffect(() => {
        if (!Object.keys(restaurantsToDisplay).length || cuisine_filter_id !== 0) getAllRestaurantsToDisplay();
    });

    return (
        <div className="popular-container">
            <div className="popular__label">Popular Restaurants in SF</div>
            <div className="popular__restaurants">
                {restaurantsToDisplay && Object.values(restaurantsToDisplay).map(restaurant => (
                    <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className="popular__restaurant">
                        <img src={restaurant.image_url}></img>
                        <div>{restaurant.name}</div>
                        <div>{restaurant.address}</div>
                    </Link>
                ))}
            </div>
        </div>
    )
}

export default Popular;