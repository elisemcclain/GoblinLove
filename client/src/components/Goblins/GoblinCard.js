import React from "react";
import { useHistory } from "react-router-dom";

function GoblinCard({ goblin }) {
  const history = useHistory();

  const navigate = () => {
    const path = `/goblins/${goblin.name}`;
    history.push(path);
  };
  return (
    <div>
      <h2>{goblin.name}</h2>
      <img src={goblin.img_url} alt={goblin.name} onClick={navigate} />
      <p>Click Image to see more!</p>
    </div>
  );
}

export default GoblinCard;
