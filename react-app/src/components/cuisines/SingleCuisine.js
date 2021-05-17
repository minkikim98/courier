import React from 'react';

import { useParams } from "react-router-dom";

const SingleCuisine = () => {
    const cuisineId = useParams();

    return (
        <div>This is the single cuisine page. The Cuisine Id is: {cuisineId}</div>
    )
}

export default SingleCuisine;