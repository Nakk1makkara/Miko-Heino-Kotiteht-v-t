#! Write a program that prompts for three integers. The program prints the sum, product and average of the numbers
// to the HTML document. (3p) remember to convert strings to numbers when adding

let num1 = parseInt(prompt("Number 1"));
let num2 = parseInt(prompt("Number 2"));
let num3 = parseInt(prompt("Number 3"));

let sum = num1 + num2 + num3
let product = num1* num2* num3
let average = sum / 3


let html = '<ol>';

{
    html += '<li>'
    html += "sum of given numbers " + sum
    html += '</li>';

}
{
    html += '<li>'
    html += "product of given numbers " + product
    html += '</li>';

}
{
    html += '<li>'
    html += "Average of given numbers " + average
    html += '</li>';

}

html += '</ol>';

let kohde = document.querySelector('#kohde');
kohde.innerHTML = html