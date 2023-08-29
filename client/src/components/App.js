import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route, useHistory } from "react-router-dom";

import GoblinContainer from "./Goblins/GoblinContainer";
import GoblinDetails from "./Goblins/GoblinDetails";
import Home from "./Home";
import Login from "./Login";
import UserPage from "./UserPage"

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
    const history = useHistory();
    setUsers(updatedUserArray);
    setCurrentUser(newUser);
    setLoggedIn(true);
    history.push(`/${newUser.username}`);
  };

  const handleLogin = (user) => {
    const history = useHistory();
    setCurrentUser(user);
    setLoggedIn(true);
    history.push(`/${user.username}`);
  }
  
  const handleChangeUser = async (user) => {
    const oldUserIndex = users.findIndex((u) => u.username === user.username);
    if (oldUserIndex !== -1) {
      try {
        const response = await fetch(`http://localhost:5555/users/${user.id}`, {
          method: "PATCH",
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
          body: JSON.stringify(user),
        });
        if (response.status === 200) {
          const updatedUserData = await response.json();
          const updatedUsers = [
            ...users.slice(0, oldUserIndex),
            ...users.slice(oldUserIndex + 1),
          ]
          const addNewUser = [...updatedUsers, updatedUserData];
          setUsers(addNewUser);
          setCurrentUser(updatedUserData);
        } else {
          console.log("Error updating user:", response.status);
        }
      } catch (error) {
        console.error("Error updating user:", error)
      }
    } else {
      console.log("User not found");
    }
  }

  const handleDeleteUser = async (user) => {
    try {
      const response = await fetch(`http://localhost:5555/users/${user.id}`, {
        method: "DELETE",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json",
        },
    })
    if (response.status === 200) {
      const updatedUsers = users.filter((u) => u.username!== user.username);
      setUsers(updatedUsers)
      setCurrentUser(null);
    } else {
      console.log("Error deleting user:", response.status);
    }
    } catch(error) {
      console.error("Error deleting user:", error)
    }

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
          <Route path = "/:userUsername">
            <UserPage users = {users} currentUser = {currentUser} handleChangeUser = {handleChangeUser} handleDeleteUser = {handleDeleteUser}/>
          </Route>
        </Switch>
      </main>
    </BrowserRouter>
  );
}

export default App;


