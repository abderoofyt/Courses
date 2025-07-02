// Code here for the callbacks task

// Setting variables to hold the intervalID and a counter.
let intervalID;
let counter = 0;

function startCounter() {
  intervalID = setInterval(function () {
    // Create the logic needed in the setInterval() function for
    // incrementing the counter and outputting to the console
    counter++;
    console.log(counter);
  }, 1000); // Adjust the interval as needed
}

function stopCounter() {
  // add the logic required to stop the counter using clearInterval()
  clearInterval(intervalID);
}

// Get references to the start and stop buttons
let startButton = document.getElementById("start");
let stopButton = document.getElementById("stop");

// Explanation:
// "document.getElementById("start")"" retrieves the element with the ID "start".
// "document.getElementById("stop")"" retrieves the element with the ID "stop".
// The retrieved elements are stored in the variables for later use.

// The event listener below is missing a callback function argument;
// this button should start the outputting of the counter to the console
startButton.addEventListener("click");

// The event listener below is missing a callback function argument;
// this button should the counter from outputting to the console
stopButton.addEventListener("click");

// Explanation:
// `startCounter` and `stopCounter` are functions that should be executed when their respective buttons are clicked.
// They need to be passed as callback functions to the `addEventListener` method.
// The callback functions will be invoked when the corresponding button is clicked, triggering the start or stop of the counter.