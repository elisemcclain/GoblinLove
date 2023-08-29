import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import Goblin from "./Goblin";
// import Login from "./Login";
import Login2 from "./Login2";
import Home from "./Home";

function App() {
  const [users, setUsers] = useState([]);
  const [goblins, setGoblins] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    fetch("http://localhost:5555/users")
      .then((r) => r.json())
      .then((userArray) => {
        setUsers(userArray);
        console.log({ users, userArray });
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
    setCurrentUser(newUser);
    setLoggedIn(true);
  };

  const handleLogin = (user) => {
    console.log(user)
    setCurrentUser(user);
    setLoggedIn(true);
  }
  

  return (
    <BrowserRouter>
      <main>
        <Switch>
          <Route exact path="/">
            <Home />
          </Route>
          <Route exact path="/login">
            {/* <Login
              onAddUser={handleAddUser}
              users={users}
              setUsers={setUsers}
            /> */}
            <Login2 users = {users} handleAddUser = {handleAddUser} handleLogin = {handleLogin}/>
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
