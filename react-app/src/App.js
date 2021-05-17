import React, { useState, useEffect } from "react";
import { useDispatch} from "react-redux";
import { BrowserRouter, Route, Switch } from "react-router-dom";
import LoginForm from "./components/auth/LoginForm";
import SignUpForm from "./components/auth/SignUpForm";
// import NavBar from "./components/NavBar";
import ProtectedRoute from "./components/auth/ProtectedRoute";
import UsersList from "./components/UsersList";
import User from "./components/User";
import MainPage from "./components/main/MainPage";
import IntroPage from "./components/IntroPage";
import SingleCuisine from "./components/cuisines/SingleCuisine";
import SingleRestaurant from "./components/restaurant/SingleRestaurant";
// import { authenticate } from "./services/auth";
import { authenticate } from "./store/session";

function App() {
  // const [authenticated, setAuthenticated] = useState(false);
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
      {/* <NavBar /> */}
      <Switch>
        <Route path="/login" exact={true}>
          <LoginForm />
        </Route>
        <Route path="/sign-up" exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path="/users" exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path="/users/:userId" exact={true} >
          <User />
        </ProtectedRoute>
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
      </Switch>
    </BrowserRouter>
  );
}

export default App;
