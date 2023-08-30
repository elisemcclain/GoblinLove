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
    window.location.href = "http://localhost:3000/login"
  }

  return (
    <div>
      <div className="gob-love">
        <h1>GOBLIN LOVE</h1>
      </div>
      <div className="enter">
        <button onClick={handleClick}>Click here to begin your journey</button>
      </div>
    </div>
  );
}

export default Home;
