import React from 'react';

import NavBar from "../navbar/NavBar"
import Categories from "./Categories"
// import Footer from "../footer/Footer"
import Popular from "./Popular"

const MainPage = () => {
    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <Popular />
            </div>
            {/* <Footer /> */}
        </div>
    )
}

export default MainPage;