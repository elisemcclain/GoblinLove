import { Link } from "react-router-dom";
import React, { useState } from "react";

function Login({ onAddUser }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userExists, setUserExists] = useState(true);
  const [errors, setErrors] = useState([]);

  function handleSubmit(e) {
    e.preventDefault();
    fetch("/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        username: username,
        email: email,
        password: password,
      }),
    })
      .then((r) => r.json())
      .then((newUser) => onAddUser(newUser));
  }
  //   console.log({ users });

  return (
    <div>
      <div>
        <h1>Welcome!</h1>
        <p>Enter your email to log in or create an account</p>
      </div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">email</label>
        <input
          type="email"
          value={email}
          placeholder="email"
          id="email"
          name="email"
          onChange={(e) => {
            setEmail(e.target.value);
            // setUserExists();
          }}
        />
        {userExists ? (
          <>
            <label htmlFor="password">password</label>
            <input
              type="password"
              value={password}
              placeholder="password"
              id="password"
              name="password"
              onChange={(e) => {
                setPassword(e.target.value);
                // setUserExists();
              }}
            />
            <button>Log In</button>
          </>
        ) : (
          <>
            <label htmlFor="username">username</label>
            <input
              type="text"
              value={username}
              placeholder="username name"
              id="username"
              name="username"
              onChange={(e) => {
                setUsername(e.target.value);
                // setUserExists();
              }}
            />
            <button>Create Account</button>
          </>
        )}
      </form>
    </div>
  );
}

export default Login;
