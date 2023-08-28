import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Goblin from "./Goblin";
import Login from "./Login";
import Home from "./Home";

function App() {
  const [users, setUsers] = useState([]);
  const [goblins, setGoblins] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5555/users")
      .then((r) => r.json())
      .then((userArray) => {
        setUsers(userArray);
      });
  }, []);

  useEffect(() => {
    fetch("http://localhost:5555/goblins")
      .then((r) => r.json())
      .then((goblinArray) => {
        setGoblins(goblinArray);
      });
  }, []);

  const handleAddUser = (newUser) => {
    const updatedUserArray = [...users, newUser];
    setUsers(updatedUserArray);
  };

  return (
    <BrowserRouter>
      <main>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/login">
            <Login onAddUser={handleAddUser} />
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
