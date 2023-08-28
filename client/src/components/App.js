import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Goblin from "./Goblin";
import Login from "./Login";
import Home from "./Home";

function App() {
  // const initialUser = {
  //   user_first_name: "",
  //   user_last_name: "",
  //   user_email: "",
  //   user_password: "",
  // };
  // const [newUser, setNewUser] = useState(initialUser);

  const [users, setUsers] = useState([]);
  const [goblins, setGoblins] = useState([]);

  useEffect(() => {
    fetch("/users")
      .then((r) => r.json())
      .then(setUsers);
  }, []);

  useEffect(() => {
    fetch("/goblins")
      .then((r) => r.json())
      .then(setGoblins);
  }, []);

  function handleAddUser(newUser) {
    setUsers((users) => [...users, newUser]);
  }

  return (
    <BrowserRouter>
      <main>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/login">
            <Login onAddUser={handleAddUser} />
            {/* {<Login setNewUser={setNewUser} newUser={newUser} />} */}
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
