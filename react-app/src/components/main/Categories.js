import React, { useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import { getCuisines } from "../../store/cuisine"

// import desserts from "../../images/cuisines/desserts.png"
import "./Categories.css"

const Categories = () => {
    const dispatch = useDispatch();

    const cuisineInfo = useSelector(state => state.cuisine)

    const getAllCuisines = async (e) => {
        await dispatch(getCuisines());
    };

    useEffect(() => {
        if (!Object.keys(cuisineInfo).length) getAllCuisines();
    });

    return (
        <div className="cuisines-container">
            {cuisineInfo && Object.values(cuisineInfo).map(cuisine => (
                <Link key={cuisine.id} to={`/cuisines/${cuisine.id}`} className="cuisine">
                    <img src={cuisine.image_url}></img>
                    {cuisine.name}
                </Link>
            ))}
        </div>
    )
}

export default Categories;