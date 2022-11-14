#! Write a program that asks for the names of six dogs.
// The program prints dog names to unordered list <ul> in reverse alphabetical order. (2p

let Dogs = [];

for (let i = 0; i < 6; i++)

{
    let Dog = prompt("Dog Name");
    Dogs.push(Dog)
}

Dogs.sort();
Dogs.reverse();


let html = '<ul>';
for (let i = 0; i < 6; i ++)

{
    html += '<li>'
    html += Dogs[i]
    html += '</li>';

}

html += '</ul>';

let kohde = document.querySelector('#kohde');
kohde.innerHTML = html