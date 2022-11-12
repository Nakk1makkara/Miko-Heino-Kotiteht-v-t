#! Write a program that asks the user for the number of participants. After this, the program asks for the names
// of all participants. Finally, the program prints the names of the participants on
// the web page in an ordered list (<ol>) in the same order as they were entered. (2p)

let nof_p = parseInt(prompt("How many participants?"));

let participants = [];

for(let i = 0; i < nof_p; i++)

{
    participants[i] = prompt("Name");
}

let html = '<ol>';
for (let i = 0; i < nof_p; i ++)

{
    html += '<li>'
    html += participants[i]
    html += '</li>';

}

html += '</ol>';

let kohde = document.querySelector('#kohde');
kohde.innerHTML = html