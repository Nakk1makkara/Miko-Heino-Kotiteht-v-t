#! Write a program that prompts the user for five numbers and prints them in the
// reverse order they were entered. Print the result to the console.(2p)
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.

let luvut = []

for (let i  = 0; i < 5; i++)
{
    luvut[i] = parseInt(prompt("anna luku" + (i+ 1)));
}

for (let i = 0; i < 5; i++)

{
    console.log(luvut[4-i])
}
