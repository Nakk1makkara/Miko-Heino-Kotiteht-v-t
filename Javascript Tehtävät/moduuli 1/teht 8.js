#! Write a program that prompts the user for the start and end year.
// The program prints all leap years from the interval given by the user.
// Printing is done in an unordered list to the HTML document. (3p)

const StartYear = Number(prompt("Enter the start year: "));
const EndYear = Number(prompt("Enter the end year: "));

let LeapYears = [];

for (let i = StartYear; i <= EndYear; i++) {
    if (i % 4 === 0 && (i % 100 !== 0 || i % 400 === 0)) {
        LeapYears.push(i);
    }
}

ul = document.getElementById("list")
for (let i = 0; i < LeapYears.length; i++) {
    li = document.createElement("li")
    li.innerHTML = LeapYears[i]
    ul.appendChild(li)
}
