import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { Formik, FormikConsumer, useFormik } from "formik";
import { useHistory } from "react-router-dom";
import * as yup from "yup";

function Login({ newUser, setNewUser, onAddUser }) {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
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
      firstName,
      lastName,
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
          setFirstName("");
          setLastName("");
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
      <img className="gob-head" src={"./GoblinHead.png"} alt="GOBSMACKED" />
      <div>
        <h1 className="welcome">WELCOME</h1>
      </div>
      <div className="greet">
        Enter your username to log in or create an account
      </div>
      <div className="signup-move">
        <button onClick={() => setLoginType(!loginType)} className="signup">
          {loginType ? "Back to Login" : "Click to Create Account"}
        </button>
      </div>
      <form onSubmit={formik.handleSubmit}>
        <br />
        {loginType && (
          <div>
            <label className="email" htmlFor="email">
              Email:{" "}
            </label>
            <input
              className="email-color"
              id="email"
              name="email"
              onChange={formik.handleChange}
              value={formik.values.email}
            />
            <p className="error-message"> {formik.errors.email}</p>
          </div>
        )}
        <label className="username" htmlFor="username">
          Username:{" "}
        </label>
        <input
          className="username-color"
          id="username"
          name="username"
          onChange={formik.handleChange}
          value={formik.values.username}
        />
        <p className="error-message-1"> {formik.errors.username}</p>
        <label className="password" htmlFor="password">
          Password:{" "}
        </label>
        <input
          className="password-color"
          id="password"
          name="password"
          onChange={formik.handleChange}
          value={formik.values.password}
        />
        <p className="error-message-2"> {formik.errors.password}</p>
        <br />
        <button className="login" type="submit">
          {loginType ? "Create Account" : "Login"}
        </button>
      </form>
    </div>
  );
};

export default Login;
