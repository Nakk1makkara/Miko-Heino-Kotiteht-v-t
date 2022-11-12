#! Write a program that prompts for user's name and then greets the user. Print the result to the HTML document: Hello, Name! (2p)

let Name = prompt("What's your name?");

let html = '<ol>';

{
    html += '<p>'
    html += "Hello!" + Name
    html += '</p>';

}

html += '</ol>';

let kohde = document.querySelector('#kohde');
kohde.innerHTML = html