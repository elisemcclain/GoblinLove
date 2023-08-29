import React, { useState } from "react";
import { Link } from "react-router-dom";
import Hamburger from "./Hamburger";

export default function NavBar() {
    const [hamburgerOpen, setHamburgerOpen] = useState(false)

    const toggleHamburger = () => {
        setHamburgerOpen(!hamburgerOpen)
    }

    return (
        <div>
            <div className="navigationr">
                <ul>
                    <li>
                        <Link to="/login">Login</Link>
                    </li>
                    <li>
                        <Link to="/goblin">Goblin Dates</Link>
                    </li>
                    <li>
                        <a href="https://www.cosmopolitan.com/" target="_blank" rel="noopener noreferrer">Tips & Tricks
                    </a>
                    </li>

                </ul>
                    <div className="hamburger">
                        <Hamburger />
                    </div>
            </div>
        </div>
  )
}




//<nav>
//         <div className="nav-bar">
//             <ul>
//                 <li>
//                     <Link to="/login">Login</Link>
//                 </li>
//                 <li>
//                 <Link to="/goblin">Goblin Dates</Link>
//                 </li>
//                 <li>
//                 <a href="https://www.cosmopolitan.com/" target="_blank" rel="noopener noreferrer">
//                     Tips & Tricks
//                 </a>
//                 </li>
//             </ul>
//         </div>
//     </nav>
//   );
// }