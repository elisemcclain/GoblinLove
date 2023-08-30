import { useParams, useHistory } from 'react-router-dom'
import { Formik, useFormik } from 'formik';
import * as Yup from 'yup';
import { useState, useEffect, useInsertionEffect } from 'react';


function UserPage({users, currentUser, handleChangeUser, handleDeleteUser}) {

    // const [edit, setEdit] = useState(false)
    // const { username } = useParams()
    // const [userMatch, setUserMatch] = useState(false)
    
    // console.log("username:", username)
    // const history = useHistory()
    // const formShema = Yup.object().shape({
    //     email: Yup.string(),
    //     username: Yup.string().required('Username is required'),
    //     password: Yup.string().required('Password is required'),
    // })

    // useEffect(() => {
    //     if (currentUser) {
    //         setUserMatch(true);
    //     }
    // }, [currentUser])

    // const EditProfile = () => {
    //     if (edit) {

    //     } else {
    //         setEdit(!edit)
    //     }
    // }
    return (
        <div>
            <p>test</p>
        </div>
    )
}

export default UserPage;