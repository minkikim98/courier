import React, { useState } from 'react';

const EditDateTime = () => {

    const [date, setDate] = useState();
    const [time, setTime] = useState();

    return (
        <div id="date-time">
            <input
                name="date"
                type="date"
                value={date}
                onChange={(e) => setDate(e.target.value)}
            />
            <input
                name="time"
                type="time"
                value={time}
                onChange={(e) => setTime(e.target.value)}
            />
        </div>
    )
}

export default EditDateTime;