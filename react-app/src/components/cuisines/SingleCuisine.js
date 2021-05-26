import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from "react-router-dom";
import { Link } from 'react-router-dom';

import { getFilteredRestaurants } from "../../store/restaurants";

import NavBar from "../navbar/NavBar";

const SingleCuisine = () => {
    const cuisineId = useParams().cuisineId;

    const dispatch = useDispatch();

    const restaurantsToDisplay = useSelector(state => state.restaurants.restaurants);

    const getFilteredRestaurantsToDisplay = async (e) => {
        await dispatch(getFilteredRestaurants(cuisineId));
    };

    useEffect(() => {
        // if (!Object.keys(restaurantsToDisplay).length) getFilteredRestaurantsToDisplay();
    });

    // getFilteredRestaurantsToDisplay();

    return (
        <div>
            <NavBar />
            <div className="main-body">
                test
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