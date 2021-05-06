const SET_ADDRESS = "session/SET_ADDRESS";
const SET_TIME = "session/SET_TIME";
const SET_DATE = "session/SET_DATE";

const initialState = { address: "", time: "", date: "" };

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_ADDRESS:
            return {  };
        case SET_TIME:
            return {  };
        case SET_DATE:
            return {  };
        default:
            return state;
    }
}