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
        document.getElementById("close-date-time").addEventListener('click', closeEditDateTime);
    }, [showEditDateTime]);

    

    return (
        <>
            <button id="edit-date-time-button"
                onClick={openEditDateTime}>
                {deliveryDateTimeInfo.dateString.concat(" ", deliveryDateTimeInfo.timeString)}
            </button>
            {showEditDateTime && <EditDateTime />}
        </>
    )
}

export default EditDateTimeButton;
