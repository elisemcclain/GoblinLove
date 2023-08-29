import { Link } from "react-router-dom";
import { useEffect, useState } from "react-router";


function GoblinCard({goblin}) {
    console.log(goblin)
    return (
        <div>
            <img src = {goblin.img_url}  alt = {goblin.name}/>
            
        </div>
    )
}

export default GoblinCard;