#! Write a voting program as described below for small-scale meeting use. (8p)
// The program asks for the number of candidates.
// Then the program asks for the names of the candidates: 'Name for candidate 1
// Store the candidates' names and initial vote count in objects like this:
// [
// {
// name: 'ellie',
// votes: 0,
// },
// {
// name: 'frank',
// votes: 0,
// },
// {
// name: 'pamela',
// votes: 0,
// }
// ]
// The program asks for the number of voters.
// The program asks each voter in turn who they will vote for. Voter shoud enter candidate name.
// If the voter enters an empty value instead of the voting number, it will be interpreted as an empty vote.
// The program announces the name of the winner and the results by printing it to the console:
// The winner is pamela with 3 votes.
// results:
// pamela: 3 votes
// frank: 1 votes
// ellie: 1 votes
// Some help:
// You need to compare votes so console log a and b to see how to get the correct property.
// someArray.sort((a, b) => {
// console.log(a, b);
// return b - a;
// });

let CandidateList = [];

let CandidateNumber = Number(prompt("How many candidates? : "));

for (let i = 0; i < CandidateNumber; i++) {

    let name = prompt(`Candidate name ${i + 1}`);
    CandidateList.push({name: name, votes: 0});
}

const Voters = Number(prompt("How many voters? : "));

for (let i = 0; i < Voters; i++) {
    let vote = prompt("Vote for candidate enter candidate Name: ");

    for (let i = 0; i < CandidateNumber; i++){
        if(vote == CandidateList[name]){
        CandidateList[vote - 1].votes++;
    }
}

CandidateList.sort((a, b) => b.votes - a.votes);


console.log(`The winner is ${CandidateList[0].name} with ${CandidateList[0].votes} votes.`);

console.log('Results:');

for (let i = 0; i < CandidateList.length; i++) {
    console.log(`${CandidateList[i].name}: ${CandidateList[i].votes} votes.`);
}






