import React from 'react';
import { useSelector } from 'react-redux';
import { Link } from 'react-router-dom';
import LogoutButton from "../../auth/LogoutButton"

import "./SidebarMenu.css"

const SidebarMenu = () => {
    const user = useSelector(state => state.session.user);

    return (
        <div id="sidebar-menu">
            <div id="close-sidebar-menu">
                <i className="fas fa-times"></i>
            </div>
            <div className="sidebar-menu-options">
                <Link className="sidebar-menu-option" to='/'>
                    Home
                </Link>
                {user && <LogoutButton />}
                {!user && <Link className="sidebar-menu-option" to='/login'> 
                    Login
                </Link>}
                {!user && <Link className="sidebar-menu-option" to='/sign-up'> 
                    Sign Up
                </Link>}
                <Link className="sidebar-menu-option" to='/about'>
                    About Us
                </Link>
            </div>
        </div>
    )
}

export default SidebarMenu;