#! Write a function that returns a random dice roll between 1 and 6.
// The function should not have any parameters. Write a main program that rolls the dice until the result is 6.
// The main program should print out the result of each roll in an unordered list (<ul>). (2p)

function Roll() {
    return Math.floor(Math.random() * 6) + 1;
}

let FinalRoll = 0;


while (FinalRoll !== 6){
    let roll = Roll;
    FinalRoll = roll;
    let html = '<ul>';

    {
        html += '<li>'
        html += FinalRoll
        html += '</li>';

    }

    html += '</ul>';

    let kohde = document.querySelector('#kohde');
    kohde.innerHTML = html
}


