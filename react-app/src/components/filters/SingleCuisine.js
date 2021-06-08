import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link } from "react-router-dom";

import { getFilteredRestaurants } from "../../store/restaurants";

import NavBar from "../navbar/NavBar";
import Categories from "../main/Categories/Categories";

import "./Filter.css"

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
                <div className="filter-container">
                    {cuisine_filter_id === cuisineId && Object.values(restaurantsToDisplay).map(restaurant => (
                        <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className="filter-restaurant">
                            <img src={restaurant.image_url} alt={restaurant.name}></img>
                            <div className="filter-restaurant__name">{restaurant.name}</div>
                            <div className="filter-restaurant__address">{restaurant.address}</div>
                        </Link>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default SingleCuisine;