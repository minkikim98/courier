import React from 'react';
import { Link } from 'react-router-dom';
import { useSelector } from 'react-redux';

import EditDateTimeButton from './datetime/EditDateTimeButton';
import SidebarMenuButton from './menu/SidebarMenuButton';
import AddressFormButton from './address/AddressFormButton';
import ShowCartButton from '../cart/ShowCartButton';

import logo from "../../images/logo.png";

import "./Navbar.css"

const NavBar = () => {
  const user = useSelector(state => state.session.user)

  return (
    <div className="navbar">
      <div className="navbar-left">
        <SidebarMenuButton />
        <EditDateTimeButton />
        <div> to </div>
        <AddressFormButton />
      </div>
      <div className="navbar-center">
        <Link to="/" className="navbar-center-item">
          <img src={logo} alt="Courier Logo"></img>
          <div>COURIER</div>
        </Link>
      </div>
      <div className="navbar-right">
        {user && <div className="navbar-welcome">Welcome, {user.username}!</div>}
        <input type="text" placeholder="Search"/>
        <ShowCartButton />
      </div>
    </div>
  );
}

export default NavBar;
