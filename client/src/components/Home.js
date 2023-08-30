import { useHistory } from "react-router-dom";
import { useEffect, useState } from "react";

function Home({ goblins }) {

  const history = useHistory();

  function handleClick() {
    const path = "/login";
    history.push(path);
  }

  const handleGoblinClick = (goblin) => {
    const path = `/goblins/${goblin.name}`
    history.push(path);
  }

  const handleGoblinClick = (goblin) => {
    const path = `/goblins/${goblin.name}`;
    history.push(path);
  };

  return (
    <div>
      <div>
        <img className="gobsmacked" src={"./Gobsmacked.png"} alt="GOBSMACKED" />
      </div>
      <div className="enter">
        <button onClick={handleClick} className="enter_button">
          Click to begin your journey
        </button>
      </div>
      <br />
      {goblins.length > 0 && (
        <div>
          {goblins.map((goblin) => {
          return <img src={goblin.img_url} alt = {goblin.name} onClick = {() => handleGoblinClick(goblin)}/>;
        })},
        </div>
      )
      }
    </div>
  );
}

export default Home;

