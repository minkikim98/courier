import React, { useState } from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

import "./AddressForm.css"

const AddressForm = () => {

    const [address, setAddress] = useState("");

    return (
        <form id="address-form">
            <div id="close-address-form">
                <i className="fas fa-times"></i>
            </div>
            <input
                id="address"
                type="text"
                value={address}
                onChange={(e) => {
                    setAddress(e.target.value);
                    // console.log(e.target.value)
                }}
            />
            <button type="submit">Change Address</button>
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
            <script
                src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBzMYt6Ab9km0cWys7kcBBDjzvY_P6O5s0&libraries=places&callback=getSuggestions" async defer>
            </script>
        </form>
    )
}

export default AddressForm;