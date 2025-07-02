// Using an array to store Person objects and sessionStorage to persist data.
let people = [];

// Load session data and initialise the dropdown menu on page load.
function myLoad() {
    let htmlSelect = document.getElementById("personList");
    htmlSelect.style.visibility = "hidden";

    // Check if this is the first time the page is loaded.
    if (sessionStorage.getItem("hasCodeRunBefore") === null) {
        // Initialise sessionStorage with an empty array and a flag for first-time load.
        sessionStorage.setItem("people", JSON.stringify(people));
        sessionStorage.setItem("hasCodeRunBefore", true);
    } else {
        // Otherwise, retrieve the people array from sessionStorage.
        people = JSON.parse(sessionStorage.getItem("people"));

        let i = 0;

        // Loop through the people array to add each person to the dropdown.
        people.forEach(function(p) {
            let optItem = document.createElement("option");
            // Display the first name of each person in the dropdown.
            optItem.innerHTML = p.name.first;
            // Assign the index as the value for each option.
            optItem.value = i;
            i += 1;
            htmlSelect.appendChild(optItem);
        });

        // Show the dropdown if at least one person exists.
        if (i > 0) {
            htmlSelect.style.visibility = "visible";
        }
    }
}

// Constructor function to create Person objects.
function Person(first, last, age, gender, interests) {
    // Set properties for the Person object.
    this.name = {
        first: first,
        last: last
    };
    this.age = age;
    this.gender = gender;
    this.interests = interests;
}

// Add a new person to the people array and update sessionStorage.
function addPerson() {
    // Retrieve the current people array from sessionStorage.
    people = JSON.parse(sessionStorage.getItem("people"));

    // Create a new Person object using data from the form.
    let newPerson = new Person(
        document.getElementById("fName").value,
        document.getElementById("lName").value,
        document.getElementById("age").value,
        document.getElementById("gender").value,
        document.getElementById("interests").value
    );

    // Add the new Person object to the people array.
    people.push(newPerson);

    // Save the updated people array to sessionStorage.
    sessionStorage.setItem("people", JSON.stringify(people));
}

// Handle the selection of a person from the dropdown and display their bio.
function ChangeActiveUser(indexOfPersonObj) {
    // Add a bio function to the selected Person object.
    people[indexOfPersonObj].bio = function() {
        // Display the person's bio with their name, age, and interests.
        alert(
            this.name.first +
            " " +
            this.name.last +
            " is " +
            this.age +
            " years old. " +
            this.name.first +
            " likes " +
            this.interests +
            "."
        );
    };

    // Call the bio method to display the selected person's information.
    people[indexOfPersonObj].bio();
}
