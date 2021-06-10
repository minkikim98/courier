import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import "./Search.css"

const Search = () => {
    const [searchText, setSearchText] = useState('');
    const [searchResults, setSearchResults] = useState([]);
    
    const allRestaurants = useSelector(state => state.restaurants.restaurants);

    useEffect(() => {
        const filteredRestaurants = (searchString) => {
            if (searchString) {
                searchString = searchString.toLowerCase();
                const filtered = Object.values(allRestaurants).filter(restaurant => {
                    return restaurant.name.toLowerCase().includes(searchString);
                });
                if (filtered.length === 0) return ['No Matches'];
                else return filtered;
            } else return []; // search term was blank
        }
        setSearchResults(filteredRestaurants(searchText))
    }, [searchText, allRestaurants]);

    let results;
    if (searchResults.length > 0) {
        if (searchResults[0] === 'No Matches') results = (<div className='search-result'>No Matches</div>);
        else results = searchResults.map(result => (
            <div key={result.id} className='search-result'>
                <Link to={`/restaurants/${result.id}`} onClick={() => setSearchText('')}>{result.name}</Link>
            </div>
        ));
    } else {
        results = (<div></div>);
    }

    return (
        <div>
            <input
                id='search-bar' 
                type='text'
                placeholder='Search Restaurants'
                onChange={e => setSearchText(e.target.value)}
                value={searchText}
            />
            {searchResults.length > 0 && <div className="auto-dropdown">
                { results }
            </div>}
        </div>
    )
}

export default Search;