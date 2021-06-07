import React, { useState, useEffect } from 'react';
import { useSelector } from "react-redux";

import EditDateTime from "./EditDateTime"

const EditDateTimeButton = () => {
    const deliveryDateTimeInfo = useSelector(state => state.delivery.dateTime);
    const [showEditDateTime, setShowEditDateTime] = useState(false);

    const openEditDateTime = () => {
        if (showEditDateTime) return;
        setShowEditDateTime(true);
    };
    
    useEffect(() => {
        if (!showEditDateTime) return;
        
        const closeEditDateTime = () => {
            setShowEditDateTime(false);
        };
        // document.addEventListener('submit', closeEditDateTime);
        document.getElementById("close-date-time").addEventListener('click', closeEditDateTime);
    }, [showEditDateTime]);

    

    return (
        <>
            <button id="edit-date-time-button"
                onClick={openEditDateTime}>
                {deliveryDateTimeInfo.toDateString() + ", " + deliveryDateTimeInfo.toLocaleTimeString("en-US").slice(0, -6) + deliveryDateTimeInfo.toLocaleTimeString("en-US").slice(-3)}
            </button>
            {showEditDateTime && <EditDateTime />}
        </>
    )
}

export default EditDateTimeButton;
