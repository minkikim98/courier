import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link } from 'react-router-dom';

import { getTaggedRestaurants } from "../../store/restaurants";

import NavBar from '../navbar/NavBar';
import Categories from '../main/Categories/Categories';

import "./Filter.css"

const SingleTag = () => {
    const tagId = useParams().tagId;
    const dispatch = useDispatch();

    const restaurantsToDisplay = useSelector(state => state.restaurants.restaurants) || {};
    const tag_filter_id = useSelector(state => state.restaurants.tag_filter_id);

    const getTaggedRestaurantsToDisplay = async (e) => {
        await dispatch(getTaggedRestaurants(tagId));
    };

    useEffect(() => {
        if (tag_filter_id !== tagId) getTaggedRestaurantsToDisplay();
    });

    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <div className="filter-container">
                    {tag_filter_id === tagId && Object.values(restaurantsToDisplay).map(restaurant => (
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

export default SingleTag;