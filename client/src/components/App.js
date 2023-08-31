import React, { useState, useEffect } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import GoblinContainer from "./Goblins/GoblinContainer";
import GoblinDetails from "./Goblins/GoblinDetails";
import Home from "./Home";
import Login from "./Login";
import UserPage from "./UserPage";
import NavBar from "./NavBar";
import Game from "./Game";

function App() {
  const [users, setUsers] = useState([]);
  const [goblins, setGoblins] = useState([]);
  const [currentUser, setCurrentUser] = useState(null);

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
        console.error("Error fetching goblin data:", error);
      }
    }
    fetchGoblins();
  }, []);
  const handleAddUser = (newUser) => {
    const updatedUserArray = [...users, newUser];
    setUsers(updatedUserArray);
    setCurrentUser(newUser);
  };

  const handleLogin = (user) => {
    console.log(user);
    setCurrentUser(user);
  };

  const handleChangeUser = async (user) => {
    setUsers([...users, user]);
    setCurrentUser(user);
  };

  const handleDeleteUser = async (user) => {
    try {
      const response = await fetch(`http://localhost:5555/users/${user.id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
      });
      if (response.status === 200) {
        const updatedUsers = users.filter((u) => u.username !== user.username);
        setUsers(updatedUsers);
        setCurrentUser(null);
      } else {
        console.log("Error deleting user:", response.status);
      }
    } catch (error) {
      console.error("Error deleting user:", error);
    }
  };

  return (
    <BrowserRouter>
      <main>
        <NavBar currentUser={currentUser} />
        <Switch>
          <Route exact path="/">
            <Home goblins={goblins} />
          </Route>
          <Route exact path="/login">
            <Login
              users={users}
              handleAddUser={handleAddUser}
              handleLogin={handleLogin}
            />
          </Route>
          <Route exact path="/goblins">
            {goblins.length > 0 ? (
              <GoblinContainer goblins={goblins} />
            ) : (
              <p>Loading goblins...</p>
            )}
          </Route>
          <Route path="/goblins/:goblinName">
            <GoblinDetails goblins={goblins} />
          </Route>
          <Route exact path="/user/:username">
            <UserPage
              users={users}
              currentUser={currentUser}
              handleChangeUser={handleChangeUser}
              handleDeleteUser={handleDeleteUser}
            />
          </Route>
          <Route exact path="/date">
            <Game currentUser={currentUser} goblins={goblins} />
          </Route>
        </Switch>
      </main>
    </BrowserRouter>
  );
}

export default App;
