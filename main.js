let string1 = "Hello";
let string2 = 'World';
let isBook= true;
let Favorites = ['yes', 'no', 'maybe'];

let characters = [
    {first_name: "Zade", last_name: "Meadows"},
    {first_name: "Feyre", last_name: "Archeron"},
    {first_name: "Rhysand", last_name: "Nightcourt"},
    {first_name:  "Lucien", last_name: "Vanserra"}
];

for (let i = 0; i < characters.length; i++) {
    if (characters[i].first_name === "Feyre") {
        characters[i].last_name = "Nightcourt";}
}

console.log(characters);

let string3 = 700 + 300;
let num = Number(string3);
console.log(typeof num);
console.log(typeof string2);
console.log(typeof isBook);
console.log(typeof Favorites);
console.log(typeof characters);

function darling(){
    return characters.map(char => {
        if (char.first_name === "Rhysand") {
            return `Hello, Feyre Darling. ${char.first_name} said.`;
        } else {
            return `Hello ${char.first_name} said`;
        }
    });
}


console.log(darling());