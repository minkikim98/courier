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
    address: addressString
})

const now = new Date();
// 825 Battery St, San Francisco, CA 94111
const initialState = { address: "825 Battery St", 
    dateTime: { 
        object: now, 
        dateString: `${now.getMonth() + 1}/${now.getDate()}/${now.getFullYear()}`, 
        timeString: now.toLocaleTimeString("en-US").slice(0, -6).concat(now.toLocaleTimeString("en-US").slice(-3))
    } 
};

export default function reducer(state = initialState, action) {
    const copyState = Object.assign({}, state);
    const obj = copyState.dateTime.object;

    switch (action.type) {
        case SET_ADDRESS:
            copyState.address = action.address;
            return copyState;
        case SET_TIME:
            obj.setMinutes(parseInt(action.minute));
            obj.setHours(parseInt(action.hour));
            copyState.dateTime.dateString = `${obj.getMonth() + 1}/${obj.getDate()}/${obj.getFullYear()}`;
            return copyState;
        case SET_DATE:
            obj.setFullYear(parseInt(action.year));
            obj.setMonth(parseInt(action.month) - 1);
            obj.setDate(parseInt(action.day));
            copyState.dateTime.timeString = now.toLocaleTimeString("en-US").slice(0, -6).concat(now.toLocaleTimeString("en-US").slice(-3));
            return copyState;
        default:
            return state;
    }
}