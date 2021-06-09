import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { setAddress } from "../../../store/delivery"
// import { GoogleMap, LoadScript } from '@react-google-maps/api';

import "./AddressForm.css"

const AddressForm = () => {
    const dispatch = useDispatch();

    const [addressState, setAddressState] = useState("");

    return (
        <form id="address-form">            
            <div>
                <i className="fas fa-times" id="close-address-form"></i>
            </div>
            <label>
                Edit your delivery address.
            </label>
            <input
                id="address"
                type="text"
                value={addressState}
                onChange={(e) => {
                    setAddressState(e.target.value);
                    dispatch(setAddress(e.target.value));
                }}
            />
            {/* <button type="submit">Change Address</button> */}
            {/* <script>
                let addressField;
                function getSuggestions() {
                    addressField = new google.maps.places.AutoComplete(
                        document.getElementById("address"),
                        {
                            types: ["establishment"]
                        }
                    )
                }
            </script> */}
            {/* <script
                src="https://maps.googleapis.com/maps/api/js?key=?????&libraries=places&callback=getSuggestions" async defer>
            </script> */}
        </form>
    )
}

export default AddressForm;