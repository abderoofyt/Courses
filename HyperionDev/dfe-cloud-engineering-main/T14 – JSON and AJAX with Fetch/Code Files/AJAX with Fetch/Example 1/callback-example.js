/*
The function 'a' takes two parameters: 'text' (a string) and 'callback' (a function). 
It demonstrates how to use a callback function by invoking 'callback' with 'text' as an argument.
In the example, function 'b' is passed as a callback when 'a' is called.
*/

function a(text, callback) {
  // Call the callback function passing in the 'text' argument.
  callback(text);
}

// This is a callback function which logs a message based on the 'text' argument.
function b(text) {
  console.log(text + "! It's me!");
}

// Call function 'a' with a predefined callback 'b'.
a("Hello world", b);

// Call function 'a' with an anonymous custom callback.
a("Hello world", function (text) {
  console.log(text + ", I can use callbacks");
});
