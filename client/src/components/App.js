import React, { useEffect, useState } from "react";
import { Switch, Route } from "react-router-dom";
import Goblin from "./Goblin";
import Home from "./Home";

// const API = "http://localhost:3000";

function App() {
  return (
    <main>
      <h1>Phase 4 Project Client</h1>
      <Switch>
        <Route exact path="/">
          <Home />
        </Route>
        <Route exact path="/goblins/:id">
          <Goblin />
        </Route>
      </Switch>
    </main>
  );
}

export default App;
