import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";

import EditDateTime from "./EditDateTime"

const EditDateTimeButton = () => {
    const dispatch = useDispatch();
    const deliveryInfo = useSelector(state => state.delivery);
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

    const now = Date.now();

    return (
        <>
            <button id="edit-date-time-button"
                onClick={openEditDateTime}>
                (Current DateTime of Delivery)
            </button>
            {showEditDateTime && <EditDateTime />}
        </>
    )
}

export default EditDateTimeButton;
