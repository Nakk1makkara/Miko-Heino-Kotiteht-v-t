#! Write a program that asks the user for an integer and tells if the number is a prime number. (2p)
// Prime numbers are numbers that are only divisible by 1 and itself.
// For example, number 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
// On the other hand, number 21 for example is not a prime number as it can be also be divided by numbers 3 and 7.
// Print the result on the HTML document.





let kohde = document.querySelector('#kohde');

let num = prompt("Give a number: ")
let prime = true;
let i;

if (num >1) {
    for (i = 2; i < num; i++) {
        if (num % i == 0) {
        prime = false;
        break;
        }
    }
}

if (prime == true){
    kohde.innerHTML = ("Selected: " + num + ". Number is a prime number")
}
else{
    kohde.innerHTML = ("Selected: " + num + ". Number is not a prime number")
}