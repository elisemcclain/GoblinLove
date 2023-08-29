import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import GoblinContainer from "./Goblins/GoblinContainer";
import GoblinDetails from "./Goblins/GoblinDetails";
import Home from "./Home";
import Login from "./Login";

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
    async function fetchGoblins() {
      try {
        const response = await fetch("http://127.0.0.1:5555/goblins");
        const goblinArray = await response.json();
        setGoblins(goblinArray);
      } catch (error) {
        console.error("Error fetching goblin data:", error)
      }
    }
    fetchGoblins();
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
            <Home goblins = {goblins}/>
          </Route>
          <Route exact path="/login">
          <Login users = {users} handleAddUser = {handleAddUser} handleLogin = {handleLogin}/>
          </Route>
          <Route exact path="/goblins">
            {goblins.length > 0 ? (
              <GoblinContainer goblins = {goblins}/>
              ) : (
                <p>Loading goblins...</p>
                )}
          </Route>
          <Route path = "/goblins/:goblinName">
            <GoblinDetails goblins = {goblins}/>
          </Route>
        </Switch>
      </main>
    </BrowserRouter>
  );
}

export default App;


