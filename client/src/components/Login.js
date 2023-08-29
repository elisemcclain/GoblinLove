import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { Formik, FormikConsumer, useFormik } from "formik";
import * as yup from "yup";


const Login = ({users, handleAddUser, handleLogin}) => {
    const [loginType, setLoginType] = useState(false)

    const formShema = yup.object().shape({
        email: yup.string(),
        username: yup.string().required("Username is required").max(20),
        password: yup.string().required("<PASSWORD>").max(20),
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

//   function Login({ onAddUser, users }) {
//     const [username, setUsername] = useState("");
//     const [email, setEmail] = useState("");
//     const [password, setPassword] = useState("");
//     const [userExists, setUserExists] = useState(true);
//     const [errors, setErrors] = useState([]);

//     function handleChange(e) {
//       const { name, value } = e.target;
//       setNewUser({ ...newUser, [name]: value });
//     }

//   function handleSubmit(e) {
//     e.preventDefault();
//     fetch(`http://localhost:5555/check-email/${email}`)
//       .then((r) => r.json())
//       .then((data) => {
//         if (data.isTaken) {
//           setUserExists(true);
//         } else {
//           fetch("http://localhost:5555/users", {
//             method: "POST",
//             headers: {
//               "Content-Type": "application/json",
//             },
//             body: JSON.stringify({
//               username: username,
//               email: email,
//               password: password,
//             }),
//           })
//             .then((r) => r.json())
//             .then((newUser) => onAddUser(newUser));
//         }
//       });
//   }

//   return (
//     <div>
//       <div>
//         <h1>Welcome</h1>
//         <h3>Enter your email to log in or create an account</h3>
//       </div>
//       <form>
//         <label htmlFor="email">email</label>
//         <input
//           type="email"
//           value={email}
//           placeholder="email"
//           id="email"
//           name="email"
//           onChange={(e) => {
//             setEmail(e.target.value);
//             setUserExists(true);
//           }}
//         />
//         {userExists ? (
//           <>
//             <label htmlFor="password">password</label>
//             <input
//               type="password"
//               value={password}
//               placeholder="password"
//               id="password"
//               name="password"
//               onChange={(e) => {
//                 setPassword(e.target.value);
//                 // setUserExists(true);
//               }}
//             />
//             <button onClick={handleSubmit}>Log In</button>
//           </>
//         ) : (
//           <>
//             <label htmlFor="username">username</label>
//             <input
//               type="text"
//               value={username}
//               placeholder="username"
//               id="username"
//               name="username"
//               onChange={(e) => {
//                 setUsername(e.target.value);
//                 // setUserExists(false);
//               }}
//             />
//             <label htmlFor="password">password</label>
//             <input
//               type="password"
//               value={password}
//               placeholder="password"
//               id="password"
//               name="password"
//               onChange={(e) => {
//                 setPassword(e.target.value);
//               }}
//             />
//             <button onClick={handleSubmit}>
//               {userExists ? "Log In" : "Create Account"}
//             </button>
//           </>
//         )}
//       </form>
//     </div>
//   );
// }

// export default Login;
