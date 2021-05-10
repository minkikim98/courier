import React, { useState, useEffect } from 'react';
import SidebarMenu from "./SidebarMenu"

const SidebarMenuButton = () => {
    const [showSidebarMenu, setShowSidebarMenu] = useState(false);

    const openSidebarMenu = () => {
        if (showSidebarMenu) return;
        setShowSidebarMenu(true);
    };

    useEffect(() => {
        if (!showSidebarMenu) return;

        const closeSidebarMenu = () => {
            setShowSidebarMenu(false);
        };

        // document.addEventListener('submit', closeEditDateTime);
        document.getElementById("close-sidebar-menu").addEventListener('click', closeSidebarMenu);
    }, [showSidebarMenu]);

    return (
        <>
            <button id="sidebar-menu-button"
                onClick={openSidebarMenu}>
                <i className="fas fa-bars"></i>
            </button>
            {showSidebarMenu && <SidebarMenu />}
        </>
    )
}

export default SidebarMenuButton;
