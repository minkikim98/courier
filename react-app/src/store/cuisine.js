const SET_CUISINES = "cuisine/SET_CUISINES";

const setCuisines = (cuisineData) => ({
    type: SET_CUISINES,
    payload: cuisineData
})

export const getCuisines = () => async (dispatch) => {
    const response = await fetch("/api/cuisines/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    dispatch(setCuisines(data));
}

const initialState = {};

export default function reducer(state=initialState, action) {
    switch (action.type) {
        case SET_CUISINES:
            return action.payload;
        default:
            return state;
    }
}