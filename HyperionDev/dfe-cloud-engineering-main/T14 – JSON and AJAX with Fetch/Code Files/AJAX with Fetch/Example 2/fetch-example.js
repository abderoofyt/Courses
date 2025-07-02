// Array to store data retrieved from the Fetch API.
let items = [];

// This function fetches data from the Google Books API.
// The fetch function returns a promise that resolves to the Response to the request.
fetch("https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699")
    .then(function(res) {
        return res.json(); // Parse the JSON response
    })
    .then(function(result) {
        items = result.items; // Store the fetched items
        console.log(items); // Log the items to the console
    })
    .catch(function(error) {
        console.log(error); // Log any errors that occur during the fetch
    });

/* 
Step 1: Rewrite the code above using arrow functions. 
Make sure to maintain the same functionality.
*/

// Insert your code for step 1 below this comment:

/* 
Step 2: Rewrite the above code using an async/await function below. 
Ensure the code works the same way as the original version.
*/

// Insert your code for step 2 below this comment:

/* 
Step 3: Copy and paste the URL for the API (https://www.googleapis.com/books/v1/volumes?q=isbn:0747532699) into your browser
to examine the data returned by Google Books. 
Now, write the code to display only the title and description of the book returned. 
You can choose to display this information either on an HTML webpage or by logging the results to the console.
*/

// Insert your code for step 3 below this comment:
