import { Link } from "react-router-dom";
import { useEffect, useState } from "react-router";

function Home({ setUsers }) {
  useEffect(() => {
    fetch("/", {
      methods: "GET",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((r) => r.json())
      .then((r) => setUsers(r))
      .catch((error) => console.log(error));
  }, []);

  function handleClick() {
    console.log("ive been clicked - create account");
  }

  return (
    <div>
      <h1>*Goblin Love*</h1>
    </div>
  );
}

export default Home;
