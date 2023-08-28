import React from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Goblin from "./Goblin";
import Login from "./Login";
import Home from "./Home";

function App() {
  return (
    <BrowserRouter>
      <main>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/login">
            <Login />
          </Route>
          <Route exact path="/goblin">
            <Goblin />
          </Route>
        </Switch>
      </main>
    </BrowserRouter>
  );
}

export default App;
