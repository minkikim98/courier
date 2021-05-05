const SET_ADDRESS = "session/SET_ADDRESS";
const SET_TIME = "session/SET_TIME";

const initialState = { address: "", time: "ASAP" };

export default function reducer(state = initialState, action) {
    switch (action.type) {
        case SET_ADDRESS:
            return {  };
        default:
            return state;
    }
}