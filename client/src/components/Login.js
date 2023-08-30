import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { Formik, FormikConsumer, useFormik } from "formik";
import { useHistory } from "react-router-dom";
import * as yup from "yup";


const Login = ({users, handleAddUser, handleLogin}) => {
    const [loginType, setLoginType] = useState(false)
    const history = useHistory()
    const formShema = yup.object().shape({
        email: yup.string(),
        username: yup.string().required("Username is required").max(20),
        password: yup.string().required("Password is required").max(100),
    })

    const formik = useFormik({
        initialValues: {
            email: "",
            username: "",
            password: "",
        },
        validationSchema: formShema,
        onSubmit: async (values) => {
            const emailExists = users.find(user => user.email.toLowerCase() === values.email.toLowerCase())
            const usernameExists = users.find(user => user.username.toLowerCase() === values.username.toLowerCase())
            if (loginType) {
                if (usernameExists) {
                    alert("Username already exists")
                }
                else if (emailExists) {
                    alert("Email already exists")
                } else {
                    try {
                        const response = await fetch('http://127.0.0.1:5555/users', {
                            method: 'POST',
                            headers: {
                                "Content-Type": "application/json",
                                Accept: "application/json",
                            },
                            body: JSON.stringify(values, null, 2),
                        })
                        if (response.status === 201) {
                            const data = await response.json()
                            console.log("User Created:", data)
                            handleAddUser(data)
                            history.push("/user")
                        } else {
                            console.log("Failed to Create User:", response.statusText)
                        }
                    } catch (error) {
                        console.error("Error Posting Users:", error)
                    }
                }
            } else {
                if (usernameExists && usernameExists.password === values.password) {
                    handleLogin(usernameExists)
                    history.push("/user")
                } else {
                    alert("Invalid Username or Password")
                }
            }
        }
    })

    return (
        <div>
            <h1>Welcome</h1>
            <button onClick={() => setLoginType(!loginType)}>{loginType ? "Click to Login" : "Click to Sign Up"}</button>
            <form onSubmit={formik.handleSubmit}>
                <br />
            {loginType && (
                <div>
                    <label htmlFor="email">Email: </label>
                    <input
                        id="email"
                        name="email"
                        onChange={formik.handleChange}
                        value={formik.values.email}
                    />
                    <p> {formik.errors.email}</p>
                </div>
            )}
                <label htmlFor="username">Username: </label>
                <input id="username" name="username" onChange={formik.handleChange} value={formik.values.username} />
                <p> {formik.errors.username}</p>
                <label htmlFor="password">Password: </label>
                <input id="password" name="password" onChange={formik.handleChange} value={formik.values.password} />
                <p> {formik.errors.password}</p>
                <br />
                <button type="submit">{loginType ? "Sign-Up" : "Login"}</button>
            </form>
        </div>
    )
}

export default Login;