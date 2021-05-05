import React from 'react';
import { Link } from 'react-router-dom';
import LogoutButton from '../auth/LogoutButton';
import EditDateTimeButton from './EditDateTimeButton'

const NavBar = () => {
  return (
    <div className="navbar">
      <div className="navbar-left">
        <button>Toggle Menu</button>
        <EditDateTimeButton />
        <div> to </div>
        <button>Delivery Address</button>
      </div>
      <div className="navbar-center">
        <Link to="/">
          Courier
        </Link>
      </div>
      <div className="navbar-right">
        <form>Search Bar</form>
        <button>Cart</button>
      </div>
      
    </div>
  );
}

export default NavBar;
