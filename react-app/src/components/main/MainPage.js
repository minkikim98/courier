import React from 'react';
import NavBar from "../navbar/NavBar"
import Categories from "./Categories"
import Footer from "../footer/Footer"

const MainPage = () => {
    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <div>National Favorites</div>
                <div>Most Popular Restaurants in SF</div>
            </div>
            <Footer />
        </div>
    )
}

export default MainPage;