/*
  This script demonstrates how to use setTimeout to trigger a function after 
  a specified delay and how to clear a timeout before it executes. 
*/

// Variable to hold the timeout identifier
let timeout;

// Function to be triggered after the timeout
function timeoutTrigger() {
    const str = "The timeout has been triggered!";
    // Set the text color to green
    const result = str.fontcolor("green");
    // Update the HTML content of the timeout_text element
    document.getElementById("timeout_text").innerHTML = result;
}

// Function to clear the timeout
function timeoutClear() {
    // Clear the existing timeout using its identifier
    clearTimeout(timeout);
    // Update the HTML content to indicate the timeout has been cleared
    document.getElementById("timeout_text").innerHTML = "The timeout has been cleared";
}

// Function to initialize the timeout
function timeoutInit() {
    // Set a timeout to trigger the timeoutTrigger function after 3 seconds
    timeout = setTimeout(timeoutTrigger, 3000);
    // Update the HTML content to indicate the timeout has started
    document.getElementById("timeout_text").innerHTML = "The timeout has been started";
}
