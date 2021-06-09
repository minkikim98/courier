import React from 'react';
import { useDispatch } from 'react-redux';
import { setTime, setDate } from "../../../store/delivery"

import "./EditDateTime.css"

const EditDateTime = () => {
    const dispatch = useDispatch();

    return (
        <div id="date-time">
            <div>
                <i className="fas fa-times" id="close-date-time"></i>
            </div>
            <label>
                Select delivery date.
            </label>
            <input
                name="date"
                type="date"
                onChange={(e) => {
                    const dateInfo = e.target.value.split("-");
                    console.log(dateInfo)
                    dispatch(setDate(dateInfo[0], dateInfo[1], dateInfo[2]));
                }}
            />
            <label>
                Select desired delivery time.
            </label>
            <input
                name="time"
                type="time"
                onChange={(e) => {
                    const timeInfo = e.target.value.split(":");
                    dispatch(setTime(timeInfo[0], timeInfo[1]));
                }}
            />
        </div>
    )
}

export default EditDateTime;