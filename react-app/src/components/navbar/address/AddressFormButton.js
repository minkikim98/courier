import React, { useState, useEffect } from 'react';
import { useDispatch, useSelector } from "react-redux";

import AddressForm from "./AddressForm"

const AddressFormButton = () => {
    const dispatch = useDispatch();
    const deliveryInfo = useSelector(state => state.delivery);
    const [showAddressForm, setShowAddressForm] = useState(false);

    const openAddressForm = () => {
        if (showAddressForm) return;
        setShowAddressForm(true);
    };

    useEffect(() => {
        if (!showAddressForm) return;

        const closeAddressForm = () => {
            setShowAddressForm(false);
        };
        // document.addEventListener('submit', closeEditDateTime);
        document.getElementById("close-address-form").addEventListener('click', closeAddressForm);
    }, [showAddressForm]);

    const now = Date.now();

    return (
        <>
            <button id="address-form-button"
                onClick={openAddressForm}>
                {deliveryInfo.address}
            </button>
            {showAddressForm && <AddressForm />}
        </>
    )
}

export default AddressFormButton;
