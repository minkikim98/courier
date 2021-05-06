import React, { useState } from 'react';

const EditDateTime = () => {

    const [date, setDate] = useState("");
    const [time, setTime] = useState("");

    return (
        <div id="date-time">
            <div id="close-date-time">X</div>
            <input
                name="date"
                type="date"
                value={date}
                onChange={(e) => {
                    setDate(e.target.value);
                    console.log(e.target.value)
                }}
            />
            <input
                name="time"
                type="time"
                value={time}
                onChange={(e) => {
                    setTime(e.target.value);
                    console.log(typeof e.target.value)
                }}
            />
        </div>
    )
}

export default EditDateTime;