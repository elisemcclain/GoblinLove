import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";

function Login({ newUser, setNewUser, onAddUser }) {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userExists, setUserExists] = useState(true);

  //   function handleChange(e) {
  //     const { name, value } = e.target;
  //     setNewUser({ ...newUser, [name]: value });
  //   }

  function handleSubmit(e) {
    e.preventDefault();
    const formData = {
      username,
      email,
      password,
    };
    fetch("/users", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    }).then((r) => {
      if (r.ok) {
        r.json().then((user) => {
          setUsername("");
          setEmail("");
          setPassword("");
          onAddUser(user);
        });
      } else {
        r.json().then((err) => setErrors(err.errors));
      }
    });
  }

  return (
    <div>
      <div>
        <h1>*Welcome! Enter your email to log in or create an account*</h1>
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
              type="email"
              value={password}
              placeholder="password"
              id="password"
              name="password"
              onChange={(e) => {
                setPassword(e.target.value);
                setUserExists(true);
              }}
            />
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
                setUserExists(false);
              }}
            />
            <label htmlFor="password">password</label>
            <input
              type="email"
              value={password}
              placeholder="password"
              id="password"
              name="password"
              onChange={(e) => {
                setPassword(e.target.value);
                setUserExists(false);
              }}
            />
          </>
        )}
        <button>Log In</button>
      </form>
    </div>
  );
}

export default Login;
