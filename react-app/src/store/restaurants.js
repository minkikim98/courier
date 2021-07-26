const SET_RESTAURANTS = "restaurants/SET_RESTAURANTS";
const SET_RESTAURANT = "restaurants/SET_RESTAURANT";

const setRestaurants = (restaurantsInfo) => ({
    type: SET_RESTAURANTS,
    restaurants: restaurantsInfo.restaurants
})

const setRestaurant = (restaurantInfo) => ({
    type: SET_RESTAURANT,
    restaurant: restaurantInfo
})

export const getAllRestaurants = () => async (dispatch) => {
    const response = await fetch("/api/restaurants/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(setRestaurants(data));
}


// Deprecated
/* 
export const getFilteredRestaurants = (cuisineId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/cuisines/${cuisineId}`, {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(setRestaurants(data));
}
 */

/* 
export const getTaggedRestaurants = (tagId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/tags/${tagId}`, {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(setRestaurants(data));
}
 */

export const getSingleRestaurant = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}`, {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(setRestaurant(data));
}

const initialState = { restaurants: {}, restaurant: {}};

export default function reducer(state = initialState, action) {
    const copyState = { ...state }
    switch (action.type) {
        case SET_RESTAURANTS:
            copyState.restaurants = action.restaurants;
            copyState.cuisine_filter_id = action.cuisine_filter_id;
            copyState.tag_filter_id = action.tag_filter_id;
            return copyState;
        case SET_RESTAURANT:
            copyState.restaurant = action.restaurant;
            return copyState;
        default:
            return state;
    }
}