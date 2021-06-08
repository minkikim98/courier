import React from "react";
import { useDispatch } from "react-redux";
import { logout } from "../../store/session";
import { clearCart } from "../../store/cart";

const LogoutButton = () => {
  const dispatch = useDispatch();
  const onLogout = async (e) => {
    await dispatch(logout());
    await dispatch(clearCart());
  };

  return <button onClick={onLogout} className="sidebar-menu-option">Logout</button>;
};

export default LogoutButton;
