import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import Hamburger from "./Hamburger";

function NavBar({ currentUser }) {
  const [hamburgerOpen, setHamburgerOpen] = useState(false);
  const [loggedIn, setLoggedIn] = useState(false);

  useEffect(() => {
    if (currentUser) {
      setLoggedIn(true);
    }
  }, [currentUser]);
  useEffect(() => {
    if (currentUser) {
      setLoggedIn(true);
    }
  }, [currentUser]);
  const toggleHamburger = () => {
    console.log(currentUser, "current user in NavBar");
    console.log(currentUser, "current user in NavBar");
    setHamburgerOpen(!hamburgerOpen);
  };

  return (
    <div>
      <div className="navigation">
        <div className="hamburger" onClick={toggleHamburger}>
          <Hamburger />
        </div>
        <div className={`menu ${hamburgerOpen ? "active" : ""}`}>
          <ul>
            <li className="links">
              <Link to="/" className="nav-link">
                Home
              </Link>
            </li>
            {loggedIn ? (
              <>
                <li>
                  <Link
                    to={`/user/${currentUser.username}`}
                    className="nav-link"
                  >
                    Profile
                  </Link>
                </li>
              </>
            ) : (
              <>
                <li>
                  <Link to="/login" className="nav-link">
                    Login
                  </Link>
                </li>
              </>
            )}
            <li>
              <Link to="/goblins" className="nav-link">
                Goblin Dates
              </Link>
            </li>
            <li>
              <a
                className="nav-link"
                href="https://www.cosmopolitan.com/"
                target="_blank"
                rel="noopener noreferrer"
              >
                Tips & Tricks
              </a>
            </li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default NavBar;
