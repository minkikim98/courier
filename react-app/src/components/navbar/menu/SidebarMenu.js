import React from 'react';
import LogoutButton from "../../auth/LogoutButton"

import "./SidebarMenu.css"

const SidebarMenu = () => {

    return (
        <div id="sidebar-menu">
            <div id="close-sidebar-menu">
                <i className="fas fa-times"></i>
            </div>
            <div className="sidebar-menu-options">
                <button className="sidebar-menu-option">
                    Home
                </button>
                <LogoutButton />
            </div>
        </div>
    )
}

export default SidebarMenu;