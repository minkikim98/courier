import React from 'react';
import LogoutButton from "../auth/LogoutButton"

const SidebarMenu = () => {

    return (
        <div id="sidebar-menu">
            <div id="close-sidebar-menu">X</div>
            <button>
                Home
            </button>
            <LogoutButton />
        </div>
    )
}

export default SidebarMenu;