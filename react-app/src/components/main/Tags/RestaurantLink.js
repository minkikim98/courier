import React from 'react';
import { Link } from 'react-router-dom';


const RestaurantLink = ({ restaurant, column }) => {
    return (
        <Link key={restaurant.id} to={`/restaurants/${restaurant.id}`} className={`tagged-restaurant__${column}`}>
            <img src={restaurant.image_url} alt={restaurant.name}></img>
            <div className="tagged-restaurant__name">{restaurant.name}</div>
            <div className="tagged-restaurant__address">{restaurant.address}</div>
        </Link>
    );
}

export default RestaurantLink;