#! Write a program that asks the user for an integer and tells if the number is a prime number. (2p)
// Prime numbers are numbers that are only divisible by 1 and itself.
// For example, number 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
// On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.
// Print the result on the HTML document.

let kohde = document.querySelector("#kohde")
let wholenumber = parseInt(prompt("Give a number and ill tell if its a prime number."))

let numero_lista = [9, 8, 7, 6, 5, 4, 3, 2]
let primenumber = false

if (wholenumber / wholenumber == 1 && wholenumber / 1 == wholenumber){
    primenumber = true
}

for (number in numero_lista)
   if (wholenumber % number == 0){
       primenumber = false
       }

if (primenumber == true){
    kohde.innerHTML = "The number is a prime number"
}

else {
    kohde.innerHTML = "The number is not a prime number"
}

