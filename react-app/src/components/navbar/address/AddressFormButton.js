import React, { useState, useEffect } from 'react';
import { useSelector } from "react-redux";

import AddressForm from "./AddressForm"

const AddressFormButton = () => {
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
        document.getElementById("close-address-form").addEventListener('click', closeAddressForm);
    }, [showAddressForm]);

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
