import { useState, useEffect } from "react";
import { Link, useHistory } from "react-router-dom";

function Game({ currentUser, goblins }) {
  const [goblin, setGoblin] = useState(null);
  const [score, setScore] = useState(0);
  const [dates, setDates] = useState([]);
  const [chosenDate, setChosenDate] = useState(null);
  const [part, setPart] = useState(1);
  const [partDesc, setPartDesc] = useState({});
  const [dialogues, setDialogues] = useState([]);
  const [responses, setResponses] = useState([]);
  const [response, setResponse] = useState(null);
  const [outcomeResult, setOutcomeResult] = useState(null);

  const history = useHistory();

  useEffect(() => {
    if (currentUser) {
      async function fetchDates() {
        try {
          const response = await fetch("http://127.0.0.1:5555/dates");
          const data = await response.json();
          setDates(data);
        } catch (error) {
          console.log("Error fetching dates", error);
        }
      }
      fetchDates();
    }
  }, [currentUser]);
  async function pickDate(date) {
    console.log(date);
    try {
      const response = await fetch("http://127.0.0.1:5555/dialogues");
      if (response.status === 200) {
        const data = await response.json();
        const usertraits = currentUser.personality_traits.map(
          (trait) => trait.id
        );
        const dialogueOptions = data.filter((dialogue) =>
          usertraits.includes(dialogue.trait_id)
        );
        const filteredDialogues = dialogueOptions.filter(
          (dialogue) => dialogue.date_id === date.id
        );
        setDialogues(filteredDialogues);
        console.log(filteredDialogues);
      } else {
        console.log("Error fetching dialogues", response.status);
      }
    } catch (error) {
      console.log("Error fetching dialogues", error);
    }
    setChosenDate(date);
    setPartDesc({
      1: date.part_1,
      2: date.part_2,
      3: date.part_3,
    });
  }
  async function handleDialogueClick(dialogue) {
    if (responses.length === 0) {
      try {
        const resp = await fetch("http://127.0.0.1:5555/responses");
        if (resp.status === 200) {
          const data = await resp.json();
          const dataResponses = data.filter(
            (res) => res.goblin_id === goblin.id
          );
          const dataResponse = dataResponses.find(
            (res) => res.dialogue_id === dialogue.id
          );
          setResponse(dataResponse);
          setResponses(dataResponses);
          setPart(part + 1);
          if (dataResponse.outcome === true) {
            setScore(score + 1);
          }
        } else {
          console.log("Error fetching responses", response.status);
        }
      } catch (error) {
        console.log("Error fetching responses", error);
      }
    } else if (part > 3) {
      try {
        const resp = await fetch("http://127.0.0.1:5555/outcomes");
        if (resp.status === 200) {
          const data = await resp.json();
          const dataOutcomes = data.filter(
            (outcome) => outcome.goblin_id === goblin.id
          );
          console.log(dataOutcomes);
          if (score === 3) {
            const dataOutcome = dataOutcomes.find(
              (outcome) =>
                outcome.date_id === chosenDate.id && outcome.result === true
            );
            setOutcomeResult(dataOutcome);
          } else {
            const dataOutcome = dataOutcomes.find(
              (outcome) =>
                outcome.date_id === chosenDate.id && outcome.result === false
            );
            setOutcomeResult(dataOutcome);
          }
        } else {
          console.log("Error fetching outcomes", response.status);
        }
      } catch (error) {
        console.log("Error fetching outcomes", error);
      }
    } else {
      const newResponse = responses.find(
        (response) => response.dialogue_id === dialogue.id
      );
      console.log(newResponse);
      setResponse(newResponse);
      setPart(part + 1);
      if (newResponse.outcome === true) {
        setScore(score + 1);
      }
    }
  }
  function endDate() {
    if (score === 3) {
      history.push(`/user/${currentUser.username}`);
    } else {
      history.push(`/user/${currentUser.username}`);
    }
  }

  return (
    <div>
      <div>
        <img className="gob-head" src={"./GoblinHead.png"} alt="GOBSMACKED" />
      </div>
      <div>
        <h1 className="gob-date-page">GOBLIN DATE</h1>
      </div>
      {currentUser ? (
        <>
          {chosenDate ? (
            <div>
              <img
                className="gob-imgs-date"
                src={goblin.img_url}
                alt={goblin.name}
              />
              <br />
              <h2>
                {part === 1
                  ? chosenDate.description
                  : response
                  ? response.response
                  : ""}
              </h2>
              <br />
              <h3>{partDesc[part]}</h3>
              <br />
              {part > 3 ? (
                <>
                  {score === 3 ? (
                    <>
                      <br />
                      <h2>
                        {outcomeResult ? outcomeResult.outcome_description : ""}
                      </h2>
                      <button onClick={endDate}>End Date 😘</button>
                    </>
                  ) : (
                    <>
                      <h2>
                        {outcomeResult ? outcomeResult.outcome_description : ""}
                      </h2>
                      <button onClick={endDate}>End Date 😒</button>
                    </>
                  )}
                </>
              ) : (
                <>
                  {dialogues
                    .filter((dialogue) => dialogue.date_part === part)
                    .map((dialogue, index) => (
                      <div>
                        <br />
                        <button onClick={() => handleDialogueClick(dialogue)}>
                          {index + 1}
                        </button>
                        <h4>{dialogue.description}</h4>
                        <br />
                      </div>
                    ))}
                </>
              )}
            </div>
          ) : (
            <div>
              {goblin ? (
                <>
                  <h3 className="what-date">
                    What date would you like to go on?
                  </h3>
                  {dates.map((date, index) => (
                    <button
                      key={index}
                      onClick={() => pickDate(date)}
                      className="date-pick-button"
                    >
                      {date.name}
                    </button>
                  ))}
                  <div className="date-space"></div>
                </>
              ) : (
                <>
                  <div>
                    <h1 className="ask-out-q">
                      Who would you like to invite out?
                    </h1>
                    <div className="gob-card-item">
                      {goblins.map((goblin, index) => (
                        <div key={index}>
                          <br />
                          <h3 className="gob-name-date">{goblin.name}</h3>
                          <img
                            className="gob-imgs-date"
                            src={goblin.img_url}
                            alt={goblin.name}
                          />
                          <button
                            className="gob-card-button"
                            onClick={() => setGoblin(goblin)}
                          >
                            Pick Me 😘
                          </button>
                          <br />
                        </div>
                      ))}
                    </div>
                  </div>
                </>
              )}
            </div>
          )}
        </>
      ) : (
        <>
          <div>
            <h2 className="login-first">Please Log In First!</h2>
          </div>
          <div>
            <Link to="/login" className="login-first-button">
              Login
            </Link>
          </div>
        </>
      )}
    </div>
  );
}

export default Game;
