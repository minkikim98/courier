import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link } from "react-router-dom";

import { getAllRestaurants } from "../../store/restaurants"


import NavBar from "../navbar/NavBar";
import Categories from "../main/Categories/Categories";

import "./Filter.css"

const SingleCuisine = () => {
    const cuisineId = useParams().cuisineId;

    const dispatch = useDispatch();

    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const cuisineRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.cuisines.some(cuisine => cuisine.cuisine_id.toString() === cuisineId));

    const getAllRestaurantsToDisplay = async (e) => {
        await dispatch(getAllRestaurants());
    };

    const allRestaurantsLoaded = () => {
        return Object.keys(allRestaurants).length;
    }

    useEffect(() => {
        if (!allRestaurantsLoaded()) getAllRestaurantsToDisplay();
    });

    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <div className="filter-container">
                    {allRestaurantsLoaded() && Object.values(cuisineRestaurants).map(restaurant => (
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