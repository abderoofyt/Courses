/*
This example shows how we use the built-in methods getElementById,
createElement, and appendChild for manipulating our HTML page.
*/

// Find and store the ordered list element in a variable called htmlList
let htmlList = document.querySelector("ol");

alert("The list items on this page were added using JavaScript! :)");

// Create and append list items to the ordered list
for (let i = 0; i < 5; i++) {
  let listItem = document.createElement("li"); // Create a list item element
  listItem.innerHTML = `I am list item number ${i + 1}`; // Set content of the list item
  htmlList.appendChild(listItem); // Append the list item to the ordered list
}
