import React from 'react';

import { useParams } from "react-router-dom";

const SingleCuisine = () => {
    const cuisineId = useParams();
    return (
        <div>This is the single cuisine page.</div>
    )
}

export default SingleCuisine;