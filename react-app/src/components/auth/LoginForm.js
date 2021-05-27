import React, { useState } from "react";
import  { useDispatch, useSelector } from "react-redux";
import { Redirect, Link } from "react-router-dom";
import { login } from "../../store/session";
import { getCart } from "../../store/cart";
import SimpleNavBar from "../navbar/SimpleNavBar";

import "./auth.css";

const LoginForm = () => {
  const dispatch = useDispatch();
  const user = useSelector(state => state.session.user);
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    await dispatch(getCart());
    if (data.errors) {
      setErrors(data.errors);
    }
  };

  const onDemoLogin = async (e) => {
    const data = await dispatch(login("demo@aa.io", "password"));
    await dispatch(getCart());
    if (data.errors) {
      setErrors(data.errors);
    }
  }

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to="/" />;
  }

  return (
    <div>
      <SimpleNavBar />
      <div className="main-body">
        <div className="auth-label">
          <div className="label-banner">Sign In</div>
          <div className="label-message">Welcome back! We're genuinely glad to see you. From late-night taco cravings to gatherings with friends, we have you covered - in an eco friendly and environmentally responsible way!</div>
          <Link to="/sign-up" className="signup-link">Don't have an account? Sign up here!</Link>
        </div>
        <form onSubmit={onLogin} id="auth-form">
          <div>
            {errors.map((error) => (
              <div className="auth-error">{error}</div>
            ))}
          </div>
          <div className="auth-form__field">
            <label htmlFor="email">Email</label>
            <input
              name="email"
              type="text"
              placeholder="Email"
              value={email}
              onChange={updateEmail}
            />
          </div>
          <div className="auth-form__field">
            <label htmlFor="password">Password</label>
            <input
              name="password"
              type="password"
              placeholder="Password"
              value={password}
              onChange={updatePassword}
            />
          </div>
          <div className="auth-form__field">
            <button type="submit">Login</button>
          </div>
          <div className="auth-form__field">
            <button onClick={onDemoLogin}>Demo Login</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
