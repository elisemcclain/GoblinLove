import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import GoblinList from "./GoblinList";

// function Goblin({goblins}) {
function Goblin() {
  const [goblins, setGoblins] = useState([]);
  useEffect(() => {
    async function fetchGoblins() {
      try {
        const response = await fetch("http://127.0.0.1:5555/goblins");
        const goblinArray = await response.json();
        setGoblins(goblinArray);
        // console.log(goblinArray)
      } catch (error) {
        console.error("Error fetching goblin data:", error);
      }
    }
    fetchGoblins();
  }, []);

  return (
    <div>
      <img className="gob-head" src={"./GoblinHead.png"} alt="GOBSMACKED" />
      <h1 className="gob-title">GOBLIN BOYS</h1>
      {goblins.length > 0 ? (
        <GoblinList goblins={goblins} />
      ) : (
        <p>Loading goblins...</p>
      )}
      {/* <GoblinList goblins = {goblins}/> */}
    </div>
  );
}

export default Goblin;
