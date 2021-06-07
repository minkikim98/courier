import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { getAllRestaurants } from "../../store/restaurants"

import NavBar from "../navbar/NavBar";
import Categories from "./Categories/Categories";
import Popular from "./Tags/Popular";
import NationalFavorites from "./Tags/NationalFavorites";
import Cultural from "./Tags/Cultural";
// import Footer from "../footer/Footer"

const MainPage = () => {
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
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <Popular />
                <NationalFavorites />
                <Cultural />
            </div>
            {/* <Footer /> */}
        </div>
    )
}

export default MainPage;