import { Link } from "react-router-dom";
import { useEffect, useState } from "react";

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
      <button onClick={handleClick}>Click here to begin your journey</button>
    </div>
  );
}

export default Home;
