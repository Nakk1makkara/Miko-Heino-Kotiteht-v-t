#! Modify the function above so that it gets the number of sides on the dice as a parameter.
// With the modified function you can for example roll a 21-sided role-playing dice.
// The difference to the last exercise is that the dice rolling in the main program continues until
// the program gets the maximum number on the dice, which is asked from the user at the beginning. (2p)

function Roll(sivut) {
    return Math.floor(Math.random() * sivut) + 1;
}

let LastRoll = 0;

const ul = document.getElementById("list");

const sides = Number(prompt("How many sides does the dice have"));

while (LastRoll !== sides){
    const roll = Roll(sides);
    LastRoll = roll;
    const li = document.createElement('li');
    li.innerText = roll;
    ul.appendChild(li);
}