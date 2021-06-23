import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
// import ProtectedRoute from "./components/auth/ProtectedRoute";
import MainPage from "./components/main/MainPage";
import IntroPage from "./components/Intro/IntroPage";
import SingleCuisine from "./components/filters/SingleCuisine";
import SingleRestaurant from "./components/restaurant/SingleRestaurant";
import SingleTag from "./components/filters/SingleTag";
// import Checkout from "./components/checkout/Checkout";

import { authenticate } from "./store/session";

function App() {
  const dispatch = useDispatch()
  const [loaded, setLoaded] = useState(false);

  useEffect(() => {
    (async() => {
      await dispatch(authenticate())
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <Route path="/" exact={true}>
          <MainPage />
        </Route>
        <Route path="/about" exact={true}>
          <IntroPage />
        </Route>
        <Route path="/cuisines/:cuisineId" exact={true}>
          <SingleCuisine />
        </Route>
        <Route path="/restaurants/:restaurantId" exact={true} >
          <SingleRestaurant />
        </Route>
        <Route path="/tags/:tagId" exact={true} >
          <SingleTag />
        </Route>
        {/* <ProtectedRoute path="/checkout" exact={true} >
          <Checkout />
        </ProtectedRoute> */}
      </Switch>
    </BrowserRouter>
  );
}

export default App;
