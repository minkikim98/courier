import React, { useState } from 'react';

const AddToCartForm = () => {
    const [quantity, setQuantity] = useState(1);

    return (
        <form>
            <div>
                <label htmlFor="quantity">Quantity</label>
                <input
                    name="quantity"
                    type="number"
                    value={quantity}
                    onChange={(e) => setQuantity(e.target.value)}
                />
            </div>
        </form>
    )
}

export default AddToCartForm;