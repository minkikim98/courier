import React, { useState, useEffect } from 'react';
import EditDateTime from "./EditDateTime"

const EditDateTimeButton = () => {
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
        
        // const closeEditDateTimeIfOutside = (e) => {
        //     console.log("inside closeedit")
        //     if (document.getElementById('edit-date-time-button').contains(e.target))
        //         openEditDateTime()
        //     else if (!document.getElementById("date-time").contains(e.target) && !document.getElementById('edit-date-time-button').contains(e.target))
        //         setShowEditDateTime(false);
        // };


        // document.addEventListener('submit', closeEditDateTime);
        document.getElementById("close-date-time").addEventListener('click', closeEditDateTime);
    }, [showEditDateTime]);

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
