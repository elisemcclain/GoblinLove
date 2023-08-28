import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Goblin from "./Goblin";
import Login from "./Login";
import Home from "./Home";

function App() {
  const [users, setUsers] = useState([]);
  const [goblins, setGoblins] = useState([]);

  const handleAddUser = (newUser) => {
    const updatedUserArray = [...users, newUser];
    setUsers(updatedUserArray);
  };

  return (
    <BrowserRouter>
      <main>
        <Switch>
          <Route exact path="/">
            <Home setUsers={setUsers} />
          </Route>
          <Route exact path="/users">
            <Login onAddUser={handleAddUser} setUsers={setUsers} />
          </Route>
          <Route exact path="/goblins">
            <Goblin />
          </Route>
        </Switch>
      </main>
    </BrowserRouter>
  );
}

export default App;
