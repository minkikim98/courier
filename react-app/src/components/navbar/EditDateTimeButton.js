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

        const closeEditDateTimeIfOutside = (e) => {
            if (document.getElementById("date-time").contains(e.target))
                setShowEditDateTime(false);
        };


        document.addEventListener('submit', closeEditDateTime);
        document.addEventListener('click', closeEditDateTimeIfOutside);

        // return () => document.getElementById("close-new-transaction-form").addEventListener('click', closeNewTransactionForm);
    }, [showEditDateTime]);

    return (
        <>
            <button className=""
                onClick={openEditDateTime}>
                (Current DateTime of Delivery)
            </button>
            {showEditDateTime && <EditDateTime />}
        </>
    )
}

export default EditDateTimeButton;
