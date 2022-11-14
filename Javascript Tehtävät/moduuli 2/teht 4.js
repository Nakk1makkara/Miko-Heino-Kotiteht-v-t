#! Write a program that asks the user for numbers until he gives zero.
// The given numbers are printed in the console from the largest to the smallest. (2p)

let Numbers = [];

let Current = 1;

while (Current !== 0) {
    Current = Number(prompt("Give a number"));
    Numbers.push(Current);
}

Numbers.sort((a, b) => b-a);

for(let i = 0; i < Numbers.length; i++) {
    console.log(Numbers[i]);
}
