#! Write a program that prompts the user for the start and end year.
// The program prints all leap years from the interval given by the user.
// Printing is done in an unordered list to the HTML document. (3p)

const start_year = Number(prompt('Enter the start year: '));
const end_year = Number(prompt('Enter the end year: '));

let leap_years = [];

for (let i = start_year; i <= end_year; i++) {
    if (i % 4 === 0 && (i % 100 !== 0 || i % 400 === 0)) {
        leap_years.push(i);
    }
}

ul = document.getElementById('list')
for (let i = 0; i < leap_years.length; i++) {
    li = document.createElement('li')
    li.innerHTML = leap_years[i]
    ul.appendChild(li)
}
