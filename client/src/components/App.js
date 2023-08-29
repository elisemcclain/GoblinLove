import React, { useEffect, useState } from "react";
import { BrowserRouter, Switch, Route } from "react-router-dom";

import GoblinContainer from "./Goblins/GoblinContainer";
// import Login from "./Login";
import Home from "./Home";

function App() {
  const [users, setUsers] = useState([]);
  const [goblins, setGoblins] = useState([]);

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
    // fetchGoblins();
    // fetch("http://127.0.0.1:5555/goblins")
    //   .then((r) => r.json())
    //   .then((goblinArray) => {
    //     setGoblins(goblinArray);
    //   });
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
          <Route exact path="/users">
            {/* <Login onAddUser={handleAddUser} users={setUsers} /> */}
          </Route>
          <Route exact path="/goblin">
            {goblins.length > 0 ? (
              <GoblinContainer goblins = {goblins}/>
              ) : (
                <p>Loading goblins...</p>
                )}
          </Route>
        </Switch>
      </main>
    </BrowserRouter>
  );
}

export default App;
