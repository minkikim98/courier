const SET_CART = "cart/SET_CART";
const CLEAR_CART = "cart/CLEAR_CART";
const SHOW_CART = "cart/SHOW_CART";
const HIDE_CART = "cart/HIDE_CART";

const setCart = (cartData) => ({
    type: SET_CART,
    payload: cartData
})

export const clearCart = () => ({
    type: CLEAR_CART,
})

export const hideCart = () => ({
    type: HIDE_CART
})

export const showCart = () => ({
    type: SHOW_CART
})

export const getCart = () => async (dispatch) => {
    const response = await fetch("/api/cart/", {
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    if (data.errors) return data; 
    dispatch(setCart(data));
    return data;
}

export const addToCart = (itemId) => async (dispatch) => {
    const response = await fetch("/api/cart/", {
        method: 'POST',
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            item_id: itemId
        })
    });
    const data = await response.json();
    if (data.errors) return data; 
    dispatch(setCart(data));
    return data;
}

export const removeFromCart = (itemId) => async (dispatch) => {
    const response = await fetch(`/api/cart/${itemId}`, {
        method: 'DELETE',
        headers: {
            "Content-Type": "application/json",
        }
    });
    const data = await response.json();
    if (data.errors) return data; 
    dispatch(setCart(data));
    return data;
}

const initialState = {cart: {}, showCart: false};

export default function reducer(state = initialState, action) {
    const copyState = Object.assign({}, state);
    switch (action.type) {
        case SET_CART:
            copyState.cart = action.payload;
            return copyState;
        case CLEAR_CART:
            return initialState;
        case SHOW_CART:
            console.log("show cart")
            copyState.showCart = true;
            return copyState;
        case HIDE_CART:
            copyState.showCart = false;
            return copyState;
        default:
            return state;
    }
}