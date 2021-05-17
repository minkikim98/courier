const SET_CART = "cart/SET_CART";

const setCart = (cartData) => ({
    type: SET_CART,
    payload: cartData
})

export const getCart = () => async (dispatch) => {
    const response = await fetch("/api/cart/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    // if (data.errors) return data; 
    dispatch(setCart(data));
    return data;
}

const initialState = {};

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_CART:
            return action.payload;
        default:
            return state;
    }
}