import React, { useState } from 'react';
import GoblinCard from './GoblinCard';

function GoblinList({goblins}) {
    console.log(goblins)
    return (
        <ul>
            {goblins.map((goblin, index) => (
                <GoblinCard goblin={goblin} key={index} />
            ))}
        </ul>
    )
}

export default GoblinList;