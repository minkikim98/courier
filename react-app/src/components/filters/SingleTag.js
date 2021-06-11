import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { useParams, Link } from 'react-router-dom';

import { getAllRestaurants } from "../../store/restaurants"

import NavBar from '../navbar/NavBar';
import Categories from '../main/Categories/Categories';
import Footer from '../footer/Footer';

import "./Filter.css"

const SingleTag = () => {
    const tagId = useParams().tagId;
    const dispatch = useDispatch();

    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const taggedRestaurants = Object.values(allRestaurants).filter((restaurant) => restaurant.tags.some(tag => tag.tag_id.toString() === tagId));

    const getAllRestaurantsToDisplay = async (e) => {
        await dispatch(getAllRestaurants());
    };

    const allRestaurantsLoaded = () => {
        return Object.keys(allRestaurants).length;
    }

    useEffect(() => {
        if (!allRestaurantsLoaded()) getAllRestaurantsToDisplay();
    });

    let tagTitleText = "";
    switch(tagId) {
        case "1":
            tagTitleText = "Popular";
            break;
        case "2":
            tagTitleText = "National Favorites";
            break;
        case "3":
            tagTitleText = "Great for Lunch";
            break;
        case "4":
            tagTitleText = "Cultural Cuisine";
            break;
        default:
            break;
    }

    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <div className="filter-title">{tagTitleText}</div>
                <div className="filter-container">
                    {allRestaurantsLoaded() && Object.values(taggedRestaurants).map(restaurant => (
                        <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className="filter-restaurant">
                            <img src={restaurant.image_url} alt={restaurant.name}></img>
                            <div className="filter-restaurant__name">{restaurant.name}</div>
                            <div className="filter-restaurant__address">{restaurant.address}</div>
                        </Link>
                    ))}
                </div>
            </div>
            <Footer />
        </div>
    )
}

export default SingleTag;