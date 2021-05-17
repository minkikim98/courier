import React from 'react';
import { Link } from 'react-router-dom';
// import LogoutButton from '../auth/LogoutButton';
import EditDateTimeButton from './datetime/EditDateTimeButton';
import SidebarMenuButton from './menu/SidebarMenuButton';
import AddressFormButton from './address/AddressFormButton';
import ShowCartButton from '../cart/ShowCartButton';

import logo from "../../images/logo.png";

import "./Navbar.css"

const NavBar = () => {
  return (
    <div className="navbar">
      <div className="navbar-left">
        <SidebarMenuButton />
        <EditDateTimeButton />
        <div> to </div>
        <AddressFormButton />
      </div>
      <div className="navbar-center">
        <img src={logo}></img>
        <Link to="/" className="navbar-center-item">
          COURIER
        </Link>
      </div>
      <div className="navbar-right">
        <input type="text" placeholder="Search"/>
        <ShowCartButton />
      </div>
    </div>
  );
}

export default NavBar;
