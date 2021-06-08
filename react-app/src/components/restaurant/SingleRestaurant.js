import React, { useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";

import { getSingleRestaurant } from "../../store/restaurants";
import { addToCart, showCart } from "../../store/cart";
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

    const addToCartCB = async (itemId) => {
        dispatch(showCart());
        await dispatch(addToCart(itemId));
    }    

    return (
        <div>
            <NavBar />
            {restaurantInfo && <div className="main-body restaurant">
                <img src={restaurantInfo.image_url} className="restaurant-banner" alt={restaurantInfo.name}></img>
                <div className="restaurant__name">{restaurantInfo.name}</div>
                <div className="restaurant__address">{restaurantInfo.address}</div>
                <div className="restaurant__description">{restaurantInfo.description}</div>
                {restaurantInfo.menus && Object.values(restaurantInfo.menus).map(menu => (
                    <div key={menu.id} className="restaurant__menu">
                        <div className="restaurant__menu-name">{menu.name}</div>
                        <div className="restaurant__menu-description">{menu.description}</div>
                        <div className="restaurant__menu-items">
                            {menu.menu_items && Object.values(menu.menu_items).map(item => (
                                <div className="restaurant__menu-item" key={item.id}>
                                    <div className="item-info">
                                        <div className="item__name">{item.name}</div>
                                        <div className="item__description">{item.description}</div>
                                        <div className="item__price">${item.price}</div>
                                        <button onClick={e => addToCartCB(item.id)}><i className="fas fa-plus"></i></button>
                                    </div>
                                    {item.image_url && <img src={item.image_url} alt={item.name}/>}
                                </div>
                            ))}
                        </div>
                    </div>
                ))}
            </div>}
        </div>
    )
}

export default SingleRestaurant;