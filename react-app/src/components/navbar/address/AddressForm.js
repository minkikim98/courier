import React, { useState } from 'react';
import { GoogleMap, LoadScript } from '@react-google-maps/api';

const AddressForm = () => {

    const [address, setAddress] = useState("");

    // const getSuggestions = () => {
    //     addressField = new google.maps.places.AutoComplete(
    //         document.getElementById("address"),
    //         {
    //             types: ["establishment"]
    //         }
    //     )
    // }


    return (
        <form id="address-form">
            <div id="close-address-form">X</div>
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
            <script async
                src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBzMYt6Ab9km0cWys7kcBBDjzvY_P6O5s0&libraries=places&callback=getSuggestions">
            </script>
        </form>
    )
}

export default AddressForm;