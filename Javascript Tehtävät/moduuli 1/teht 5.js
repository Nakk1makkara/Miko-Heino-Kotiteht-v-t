#! Write a program that asks the user to enter a year and notifies the user whether the input
// year is a leap year. A year is a leap year if it is divisible by four. However,
// years divisible by 100 are leap years only if they are also divisible by 400. Print the result on the HTML document. (3p)

let i = parseInt(prompt("Enter a year"));


let kohde = document.querySelector('#kohde');

if ((i % 4 == 0 && i % 100 != 0) || (i % 400 == 0)){
    kohde.innerHTML = "the year is a leap year";
}

else{
    kohde.innerHTML = "The year is a normal year";
}