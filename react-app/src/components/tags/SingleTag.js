import React from 'react';

import NavBar from '../navbar/NavBar';
import Categories from '../main/Categories/Categories';

const SingleTag = () => {
    return (
        <div>
            <NavBar />
            <div className="main-body">
                <Categories />
                <div className="tag-container">
                    single tag page.
                </div>
            </div>
        </div>
    )
}

export default SingleTag;