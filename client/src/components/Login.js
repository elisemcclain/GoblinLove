import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";

function Login({ newUser, setNewUser, onAddUser }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userExists, setUserExists] = useState(true);
  const [errors, setErrors] = useState([]);

  function handleChange(e) {
    const { name, value } = e.target;
    setNewUser({ ...newUser, [name]: value });
  }

  function handleSubmit(e) {
    e.preventDefault();

    fetch(`http://localhost:5555/check-email/${email}`)
      .then((r) => r.json())
      .then((data) => {
        if (data.isTaken) {
          setUserExists(true);
        } else {
          fetch("http://localhost:5555/users", {
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
      });
  }

  return (
    <div>
      <div>
        <h1>Welcome</h1>
        <h3>Enter your email to log in or create an account</h3>
      </div>
      <form>
        <label htmlFor="email">email</label>
        <input
          type="email"
          value={email}
          placeholder="email"
          id="email"
          name="email"
          onChange={(e) => {
            setEmail(e.target.value);
            setUserExists(true);
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
                // setUserExists(true);
              }}
            />
            <button onClick={handleSubmit}>Log In</button>
          </>
        ) : (
          <>
            <label htmlFor="username">username</label>
            <input
              type="text"
              value={username}
              placeholder="username"
              id="username"
              name="username"
              onChange={(e) => {
                setUsername(e.target.value);
                // setUserExists(false);
              }}
            />
            <label htmlFor="password">password</label>
            <input
              type="password"
              value={password}
              placeholder="password"
              id="password"
              name="password"
              onChange={(e) => {
                setPassword(e.target.value);
              }}
            />
            <button onClick={handleSubmit}>
              {userExists ? "Log In" : "Create Account"}
            </button>
          </>
        )}
      </form>
    </div>
  );
}

export default Login;
