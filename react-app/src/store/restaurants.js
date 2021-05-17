const SET_RESTAURANTS = "restaurants/SET_RESTAURANTS";
const SET_RESTAURANT = "restaurants/SET_RESTAURANT";

const setRestaurants = (restaurants) => ({
    type: SET_RESTAURANTS,
    payload: restaurants
})

const setRestaurant = (restaurant) => ({
    type: SET_RESTAURANT,
    payload: restaurant
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

export const getSingleRestaurant = (restaurantId) => async (dispatch) => {
    const response = await fetch(`/api/restaurants/${restaurantId}`, {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(setRestaurant(data));
}

const initialState = { restaurants: {}, restaurant: {} };

export default function reducer(state = initialState, action) {
    const copyState = { ...state }
    switch (action.type) {
        case SET_RESTAURANTS:
            copyState.restaurants = action.payload;
            return copyState;
        case SET_RESTAURANT:
            copyState.restaurant = action.payload;
            return copyState;
        default:
            return state;
    }
}