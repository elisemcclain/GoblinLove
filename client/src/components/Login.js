import { Link } from "react-router-dom";
import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as yup from "yup";
export const Login = ({ users, setUsers }) => {
    const [refreshPage, setRefreshPage] = useState(false);
    const [userExists, setUserExists] = useState(false);

    useEffect(() => {
        console.log("fetched");
        fetch("http://127.0.0.1:5555/users")
            .then((res) => res.json())
            .then((data) => {
                setUsers(data);
                console.log({ data });
            });
    }, [refreshPage]);

    const formSchema = yup.object().shape({
        email: yup.string().email("Invalid email").required("Must enter email"),
        username: yup.string().required("Must enter a username").max(20),
        password: yup.string().required("Must enter a password").max(20),
    });

    const formik = useFormik({
        initialValues: {
            username: "",
            email: "",
            password: "",
        },
        validationSchema: formSchema,
        onSubmit: (values) => {
            fetch("http://127.0.0.1:5555/users", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    Accept: "application/json",
                },
                body: JSON.stringify(values, null, 2),
            })
                .then((res) => {
                    if (res.status == 201) {
                        // account created
                        console.log("account made");
                        setRefreshPage(!refreshPage);
                        setUserExists(true);
                    }
                })
                .catch((error) => {
                    console.error("Error:", error);
                });
        },
    });

    return (
        <div>
            <h1>Welcome</h1>
            <p>Enter your email to login or create an account</p>
            <form onSubmit={formik.handleSubmit}>
                <label htmlFor="email">Email</label>
                <br />
                <input
                    id="email"
                    name="email"
                    onChange={formik.handleChange}
                    value={formik.values.email}
                />
                <p> {formik.errors.email}</p>
                <label htmlFor="username">Username</label>
                <br />
                {userExists ? (
                    <>
                        <label htmlFor="password">Password</label>
                        <br />
                        <input
                            id="password"
                            name="password"
                            onChange={formik.handleChange}
                            value={formik.values.password}
                        />
                        <p> {formik.errors.password}</p>
                        <button type="submit">Submit</button>
                    </>
                ) : (
                    <>
                        <input
                            id="username"
                            username="username"
                            onChange={formik.handleChange}
                            value={formik.values.username}
                        />
                        <p> {formik.errors.username}</p>
                        <button type="submit">Create Account</button>
                    </>
                )}
            </form>
        </div>
    );
};

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
