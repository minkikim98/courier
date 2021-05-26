import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from "react-router-dom";
import { Link } from 'react-router-dom';

import { getFilteredRestaurants } from "../../store/restaurants";

import NavBar from "../navbar/NavBar";
import Categories from "../main/Categories";

const SingleCuisine = () => {
    const cuisineId = useParams().cuisineId;

    const dispatch = useDispatch();

    const restaurantsToDisplay = useSelector(state => state.restaurants.restaurants) || {};
    const cuisine_filter_id = useSelector(state => state.restaurants.cuisine_filter_id);

    const getFilteredRestaurantsToDisplay = async (e) => {
        await dispatch(getFilteredRestaurants(cuisineId));
    };

    useEffect(() => {
        if (cuisine_filter_id !== cuisineId) getFilteredRestaurantsToDisplay();
    });

    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <div>
                    {restaurantsToDisplay && Object.values(restaurantsToDisplay).map(restaurant => (
                        <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className="popular__restaurant">
                            <img src={restaurant.image_url}></img>
                            <div>{restaurant.name}</div>
                            <div>{restaurant.address}</div>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default SingleCuisine;