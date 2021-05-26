import React from 'react';
import { Link } from 'react-router-dom';
import LogoutButton from "../../auth/LogoutButton"

import "./SidebarMenu.css"

const SidebarMenu = () => {

    return (
        <div id="sidebar-menu">
            <div id="close-sidebar-menu">
                <i className="fas fa-times"></i>
            </div>
            <div className="sidebar-menu-options">
                <Link className="sidebar-menu-option" to='/'>
                    Home
                </Link>
                <LogoutButton />
                <Link className="sidebar-menu-option" to='/login'> 
                    Login
                </Link>
                <Link className="sidebar-menu-option" to='/signup'> 
                    Sign Up
                </Link>
            </div>
        </div>
    )
}

export default SidebarMenu;