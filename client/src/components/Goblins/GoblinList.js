import React, { useState } from 'react';
import GoblinCard from './GoblinCard';

function GoblinList({goblins}) {
    console.log(goblins)
    const rendergoblins = () => {
        {goblins.map((goblin, index) => (
            // console.log(goblin),
            <GoblinCard goblin = {goblin} key={index}/>
        ))}
    }
    return (
        <ul>
            {goblins.map((goblin, index) => (
                <GoblinCard goblin={goblin} key={index} />
            ))}
        </ul>
    )
}

export default GoblinList;