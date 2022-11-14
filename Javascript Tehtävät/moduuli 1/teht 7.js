#! Write a program that asks the user for the number of dice rolls.
// The program throws all the dice once and prints the sum of the numbers. (2p)

let kohde = document.querySelector("#kohde")

let NumberOfDice = Number(prompt("Give me the amount of dice"))
let SumOfDice = 0
let sumList = []

for (let i = 0; i < NumberOfDice; i++) {
    sumList.push(Math.floor(Math.random() * 6) + 1)
}
for (let i = 0; i < sumList.length; i++) {
    SumOfDice += sumList[i]
}
console.log(SumOfDice)
console.log(sumList)
kohde.innerHTML = SumOfDice