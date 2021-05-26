import React, { useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { getSingleRestaurant } from "../../store/restaurants";
import NavBar from "../navbar/NavBar"

import "./SingleRestaurant.css"

const SingleRestaurant = () => {
    const dispatch = useDispatch();
    const restaurantInfo = useSelector(state => state.restaurants.restaurant)
    const restaurantId = useParams().restaurantId; 

    const getRestaurantInfo = async (e) => {
        await dispatch(getSingleRestaurant(restaurantId));
    };

    useEffect(() => {
        if (restaurantInfo.id !== parseInt(restaurantId)) getRestaurantInfo();
    });

    const addToCart = (itemId) => {
        console.log(itemId)
    }    

    return (
        <div>
            <NavBar />
            {restaurantInfo && <div className="main-body">
                <img src={restaurantInfo.image_url} className="restaurant-banner"></img>
                <div className="restaurant__name">{restaurantInfo.name}</div>
                <div className="restaurant__address">{restaurantInfo.address}</div>
                <div className="restaurant__description">{restaurantInfo.description}</div>
                {restaurantInfo.menus && Object.values(restaurantInfo.menus).map(menu => (
                    <div key={menu.id} className="restaurant__menu">
                        <div>{menu.name}</div>
                        {menu.menu_items && Object.values(menu.menu_items).map(item => (
                            <div className="restaurant__menu-item" key={item.id}>
                                <div>{item.name}</div>
                                <div>{item.description}</div>
                                <div>${item.price}</div>
                                <button onClick={e => addToCart(item.id)}>+</button>
                            </div>
                        ))}

                    </div>
                ))}
            </div>}
        </div>
    )
}

export default SingleRestaurant;