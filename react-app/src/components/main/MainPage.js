import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllRestaurants } from "../../store/restaurants"

import NavBar from "../navbar/NavBar";
import Categories from "./Categories/Categories";
import Popular from "./Tags/Popular";
import NationalFavorites from "./Tags/NationalFavorites";
import Cultural from "./Tags/Cultural";
import Lunch from "./Tags/Lunch";
// import Footer from "../footer/Footer"

const MainPage = () => {
    const dispatch = useDispatch();

    const allRestaurants = useSelector(state => state.restaurants.restaurants) || {};
    const cuisine_filter_id = useSelector(state => state.restaurants.cuisine_filter_id);
    const tag_filter_id = useSelector(state => state.restaurants.tag_filter_id);

    const getAllRestaurantsToDisplay = async (e) => {
        await dispatch(getAllRestaurants());
    };

    const allRestaurantsLoaded = () => {
        return Object.keys(allRestaurants).length && cuisine_filter_id === 0 && tag_filter_id === 0;
    }

    useEffect(() => {
        if (!allRestaurantsLoaded()) getAllRestaurantsToDisplay();
    });

    return (
        <div>
            <NavBar />
            <div className="main-body">
                {allRestaurantsLoaded() && <div>
                    <Categories />
                    <Popular />
                    <NationalFavorites />
                    <Lunch />
                    <Cultural />
                </div>}
            </div>
            {/* <Footer /> */}
        </div>
    )
}

export default MainPage;