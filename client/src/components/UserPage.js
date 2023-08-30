import { useParams, useHistory } from 'react-router-dom'
import { Formik, useFormik } from 'formik';
import * as Yup from 'yup';
import { useState, useEffect, useInsertionEffect } from 'react';


function UserPage({users, currentUser, handleChangeUser, handleDeleteUser}) {

    const [edit, setEdit] = useState(false)
    const { username } = useParams()
    const [userMatch, setUserMatch] = useState(false)
    const [traitAssociations, setTraitAssociations] = useState([])
    const history = useHistory()
    const formShema = Yup.object().shape({
        email: Yup.string(),
        username: Yup.string().required('Username is required'),
        password: Yup.string().required('Password is required'),
    })

    useEffect(() => {
        if (currentUser.username.toLowerCase() === username.toLowerCase()) {
            async function fetchTraitAssociations() {
                try {
                    const response = await fetch(`http://127.0.0.1:5555/trait_associations?user_id=${currentUser.id}`);
                    const data = await response.json();
                    setTraitAssociations(data)
                    console.log(data)
                } catch (error) {
                    console.log('Error fetching trait associations:', error)
                }
            }
            fetchTraitAssociations()
            setUserMatch(true);
        }
    }, [currentUser])

    const formik = useFormik({
        initialValues: {
            id: currentUser.id,
            email: currentUser.email || '',
            username: currentUser.username || '',
            password: '',
        },
        validationSchema: formShema,
        onSubmit: async (values) => {

            try {
                const response = await fetch(`http://127.0.0.1:5555/users/${currentUser.id}`, {
                    method: 'PATCH',
                    headers: {
                        'Content-Type': 'application/json',
                        Accept: 'application/json',
                    },
                    body: JSON.stringify(values),
                });
                if (response.status === 200) {
                    const updatedUserData = await response.json();
                    handleChangeUser(updatedUserData)
                } else {
                    console.error('Error updating user:', response.status)
                }
            } catch (error) {
                console.error('Error updating user:', error)
            } finally {
                setEdit(!edit)
            }
        },
    })

    const EditProfile = () => {
        if (edit) {
            formik.handleSubmit()
        } else {

            setEdit(!edit)
        }
    }

    return (
        <div>
            {currentUser ? (
                <div>
                    <button type="button" onClick={EditProfile}>{edit ? "Save Profile" : "Edit Profile" }</button>
                    {edit ? (
                        <div>
                            <form onSubmit={formik.handleSubmit}>
                                <br />
                                <div>
                                    <lable>Email</lable>
                                    <input 
                                    type="email" 
                                    onChange = {formik.handleChange} 
                                    onBlur = {formik.handleBlur} 
                                    {...formik.getFieldProps('email')} />
                                    {formik.touched.email && formik.errors.email ? (
                                        <div>{formik.errors.email}</div>
                                    ) : null}
                                </div>
                                <br />
                                <div>
                                    <label>Username</label>
                                    <input type="text" 
                                    onChange = {formik.handleChange} 
                                    onBlur = {formik.handleBlur} 
                                    {...formik.getFieldProps('username')} />
                                    {formik.touched.username && formik.errors.username ? (
                                        <div>{formik.errors.username}</div>
                                    ) : null}
                                </div>
                                <br />
                                <div>
                                    <label>Password</label>
                                    <input type="password" 
                                    onChange = {formik.handleChange} 
                                    onBlur = {formik.handleBlur} 
                                    {...formik.getFieldProps('password')} />
                                    {formik.touched.password && formik.errors.password ? (
                                        <div>{formik.errors.password}</div>
                                    ) : null}
                                </div>
                                <br />
                            </form>
                        </div>
                    ) : (
                        <div>
                            <h3>
                                Username: {currentUser.username}
                            </h3>
                            <h3>
                                Email: {currentUser.email}
                            </h3>
                            <h3>
                                Password: 🤣
                            </h3>
                            <h4>
                                Successful Dates with Grubnub: {currentUser.grubnub_win}
                            </h4>
                            <h4>
                                Successful Dates with Sneezle: {currentUser.sneezle_win}
                            </h4>
                            <h4>
                                Successful Dates with Blort: {currentUser.blort_win}
                            </h4>
                            <h4>
                                Successful Dates with Grimble: {currentUser.grimble_win}
                            </h4>
                            <h4>
                                Successful Dates with Zongo: {currentUser.zongo_win}
                            </h4>
                            <br />
                            <h3>Personality Traits: </h3>
                            <ul>
                                {traitAssociations.map(trait => {
                                    return (
                                        <li key={trait.trait.id}>{trait.trait.name}</li>
                                    )
                                })}
                            </ul>
                        </div>
                    )}
                </div>
            ) : (
                <div>
                    <h2>Not Logged in as current user at this path</h2>
                </div>
            )}
        </div>
    )
}

export default UserPage;