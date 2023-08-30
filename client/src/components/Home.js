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

  return (
    <div>
      <h1>*Goblin Love*</h1>
      <button onClick={handleClick}>Click here to begin your journey</button>
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
