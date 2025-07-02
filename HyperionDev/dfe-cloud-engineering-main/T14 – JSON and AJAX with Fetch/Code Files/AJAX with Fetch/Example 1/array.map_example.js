/* 
This example demonstrates how to use the map method to create <p> elements 
for each item in the terms array, displaying them on the page. 
*/

// Storing the array of terms in a variable.
const terms = ["JavaScript", "Node", "React", "Express", "MongoDB"];

// Creating a new div element.
let div = document.createElement("div");

// Storing the log element in a variable.
let log = document.getElementById('log');

// Use the map method to create <p> elements for each term.
terms.map(function(name) {
    let p = document.createElement("p");
    p.innerHTML = name;

    // Appending the <p> elements to the div.
    div.appendChild(p);
});

// Append the div containing <p> elements to the log div.
log.appendChild(div);
