import { useParams, useHistory } from "react-router-dom";

function GoblinDetails({ goblins }) {
  const { goblinName } = useParams();
  const history = useHistory();
  const pickedGoblin = goblins.filter(
    (goblin) => goblin.name === goblinName
  )[0];

  const navigateBack = () => {
    history.goBack();
  };

  return (
    <div>
      <img className="gob-head" src={"/GoblinHead.png"} alt="GOBSMACKED" />
      <div>
        <h1 className="gob-name-detail">{goblinName}</h1>
      </div>
      {pickedGoblin ? (
        <div>
          {/* <h1>{goblinName}</h1> */}
          <img
            className="gob-pic-det"
            src={pickedGoblin.img_url}
            alt={pickedGoblin.name}
            onClick={navigateBack}
          />
          <h5 className="artist-det">Artist: {pickedGoblin.artist}</h5>
          <p className="desc-det">{pickedGoblin.description}</p>
        </div>
      ) : (
        <div>
          <h1>No Goblin Found with this name</h1>
        </div>
      )}
    </div>
  );
}

export default GoblinDetails;
