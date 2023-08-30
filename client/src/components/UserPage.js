import { useParams, useHistory } from "react-router-dom";
import { Formik, useFormik } from "formik";
import * as Yup from "yup";
import { useState, useEffect, useInsertionEffect } from "react";

function UserPage({ users, currentUser, handleChangeUser, handleDeleteUser }) {
  const [edit, setEdit] = useState(false);
  const { username } = useParams();
  const [userMatch, setUserMatch] = useState(false);
  const [traitAssociations, setTraitAssociations] = useState([]);
  const [traits, setTraits] = useState([]);
  const history = useHistory();
  const formShema = Yup.object().shape({
    email: Yup.string(),
    username: Yup.string().required("Username is required"),
    password: Yup.string().required("Password is required"),
  });

  useEffect(() => {
    if (currentUser.username.toLowerCase() === username.toLowerCase()) {
      async function fetchTraitAssociations() {
        try {
          const response = await fetch(
            `http://127.0.0.1:5555/trait_associations?user_id=${currentUser.id}`
          );
          const data = await response.json();
          setTraitAssociations(data);
          console.log(data);
        } catch (error) {
          console.log("Error fetching trait associations:", error);
        }
      }
      fetchTraitAssociations();
      async function fetchTraits() {
        try {
          const response = await fetch(`http://127.0.0.1:5555/traits`);
          const data = await response.json();
          setTraits(data);
          console.log(data);
        } catch (error) {
          console.log("Error fetching traits:", error);
        }
      }
      fetchTraits();
      setUserMatch(true);
    }
  }, [currentUser]);

  const formik = useFormik({
    initialValues: {
      id: currentUser.id,
      email: currentUser.email || "",
      username: currentUser.username || "",
      password: "",
      traits: {},
    },
    validationSchema: formShema,
    onSubmit: async (values) => {
      const updateData = {
        id: values.id,
        email: values.email,
        username: values.username,
        password: values.password,
      };
      try {
        const response = await fetch(
          `http://127.0.0.1:5555/users/${currentUser.id}`,
          {
            method: "PATCH",
            headers: {
              "Content-Type": "application/json",
              Accept: "application/json",
            },
            body: JSON.stringify(updateData),
          }
        );
        if (response.status === 200) {
          const updatedUserData = await response.json();
          handleChangeUser(updatedUserData);
        } else {
          console.error("Error updating user:", response.status);
        }
      } catch (error) {
        console.error("Error updating user:", error);
      } finally {
        setEdit(!edit);
      }
    },
  });

  const EditProfile = async () => {
    if (edit) {
      await formik.handleSubmit();
      const existingTraitIds = traitAssociations.map(
        (association) => association.trait_id
      );
      const selectedTraits = Object.entries(formik.values.traits)
        .filter(
          ([traitId, isChecked]) =>
            isChecked && !existingTraitIds.includes(Number(traitId))
        )
        .map(([traitId]) => Number(traitId));
      try {
        for (const traitId of selectedTraits) {
          const response = await fetch(
            `http://127.0.0.1:5555/trait_associations`,
            {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
                Accept: "application/json",
              },
              body: JSON.stringify({
                user_id: currentUser.id,
                trait_id: traitId,
              }),
            }
          );
          if (response.status === 201) {
            const data = await response.json();
            setTraitAssociations((prevAssociations) => [
              ...prevAssociations,
              data,
            ]);
            console.log("Trait associations created successfully!");
          } else {
            console.error(
              "Error creating trait associations:",
              response.status
            );
          }
        }
      } catch (error) {
        console.error("Error creating trait associations:", error);
      }
    } else {
      setEdit(!edit);
    }
  };

  return (
    <div>
      <div>
        <img
          className="gob-head-user"
          src={"client/public/GoblinHead.png"}
          alt="GOBSMACKED"
        />
      </div>
      <div className="bar-user"></div>
      {currentUser ? (
        <div>
          <div className="edit-prof-button custom-edit-button-move">
            <button
              type="button"
              onClick={EditProfile}
              className="edit-prof-button custom-edit-button"
            >
              {edit ? "Save Profile" : "Edit Profile"}
            </button>
          </div>
          <div className="bar-background">
            {edit ? (
              <div>
                <form onSubmit={formik.handleSubmit}>
                  <br />
                  <div>
                    <lable>Email</lable>
                    <input
                      type="email"
                      onChange={formik.handleChange}
                      onBlur={formik.handleBlur}
                      {...formik.getFieldProps("email")}
                    />
                    {formik.touched.email && formik.errors.email ? (
                      <div>{formik.errors.email}</div>
                    ) : null}
                  </div>
                  <br />
                  <div>
                    <label>Username</label>
                    <input
                      type="text"
                      onChange={formik.handleChange}
                      onBlur={formik.handleBlur}
                      {...formik.getFieldProps("username")}
                    />
                    {formik.touched.username && formik.errors.username ? (
                      <div>{formik.errors.username}</div>
                    ) : null}
                  </div>
                  <br />
                  <div>
                    <label>Password</label>
                    <input
                      type="password"
                      onChange={formik.handleChange}
                      onBlur={formik.handleBlur}
                      {...formik.getFieldProps("password")}
                    />
                    {formik.touched.password && formik.errors.password ? (
                      <div>{formik.errors.password}</div>
                    ) : null}
                  </div>
                  <br />
                </form>
                <div>
                  <label>Personality Traits</label>
                  {traits.map((trait) => (
                    <div key={trait.id}>
                      <input
                        type="checkbox"
                        id={`trait-${trait.id}`}
                        onChange={() => {
                          formik.setFieldValue(
                            `traits.${trait.id}.checked`,
                            !formik.values.traits[trait.id]
                          );
                        }}
                        onBlur={formik.handleBlur}
                        checked={formik.values.traits[trait.id]}
                      />
                      <label htmlFor={`trait-${trait.id}`}>{trait.name}</label>
                    </div>
                  ))}
                </div>
              </div>
            ) : (
              <div>
                <h3>Username: {currentUser.username}</h3>
                <h3>Email: {currentUser.email}</h3>
                <h3>Password: 🤣</h3>
                <h4>
                  Successful Dates with Grubnub: {currentUser.grubnub_win}
                </h4>
                <h4>
                  Successful Dates with Sneezle: {currentUser.sneezle_win}
                </h4>
                <h4>Successful Dates with Blort: {currentUser.blort_win}</h4>
                <h4>
                  Successful Dates with Grimble: {currentUser.grimble_win}
                </h4>
                <h4>Successful Dates with Zongo: {currentUser.zongos_win}</h4>
                <br />
                <h3>Personality Traits: </h3>
                <ul>
                  {traitAssociations.map((trait) => {
                    return <li key={trait.trait.id}>{trait.trait.name}</li>;
                  })}
                </ul>
              </div>
            )}
          </div>
        </div>
      ) : (
        <div>
          <h2>Not Logged in as current user at this path</h2>
        </div>
      )}
    </div>
  );
}

export default UserPage;
