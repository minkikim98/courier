const SET_ADDRESS = "delivery/SET_ADDRESS";
const SET_TIME = "delivery/SET_TIME";
const SET_DATE = "delivery/SET_DATE";

export const setTime = (hour, minute) => ({
    type: SET_TIME,
    hour,
    minute
})

export const setDate = (year, month, day) => ({
    type: SET_DATE,
    year,
    month, 
    day
})

export const setAddress = (addressString) => ({
    type: SET_ADDRESS,
    payload: addressString
})

const now = new Date();
// 825 Battery St, San Francisco, CA 94111
const initialState = { address: "825 Battery St", dateTime: now };

export default function reducer(state = initialState, action) {
    const copyState = { ...state }
    switch (action.type) {
        case SET_ADDRESS:
            copyState.address = action.payload;
            return copyState;
        case SET_TIME:
            copyState.dateTime.setMinutes(parseInt(action.minute));
            copyState.dateTime.setHours(parseInt(action.hour));
            return copyState;
        case SET_DATE:
            // console.log(parseInt(action.year))
            copyState.dateTime.setFullYear(parseInt(action.year));
            copyState.dateTime.setMonth(parseInt(action.month) - 1);
            copyState.dateTime.setDate(parseInt(action.day));
            // console.log(copyState)
            return copyState;
        default:
            return state;
    }
}