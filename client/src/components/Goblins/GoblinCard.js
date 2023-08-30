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
      <h2 className="gob-name">{goblin.name}</h2>
      <img
        className="gob-imgs-boys"
        src={goblin.img_url}
        alt={goblin.name}
        onClick={navigate}
      />
      <p className="see-more">Click to see more!</p>
    </div>
  );
}

export default GoblinCard;
