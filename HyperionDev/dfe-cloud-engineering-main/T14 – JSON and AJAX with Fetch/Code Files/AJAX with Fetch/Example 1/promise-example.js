// Initialise a counter for the number of promises created.
let promiseCount = 0;

// Function to create and test a promise
function testPromise() {
  const currentPromiseCount = ++promiseCount; // Increment promise count

  const log = document.getElementById("log");
  // Insert a message indicating the promise has started, using 'beforeend' to add it as the last child.
  log.insertAdjacentHTML(
    "beforeend",
    `${currentPromiseCount}) Started (<small>Sync code started</small>)<br/>`
  );

  // Create a Promise object
  const p1 = new Promise((resolve, reject) => {
    // Insert a message indicating the promise is now started
    log.insertAdjacentHTML(
      "beforeend",
      `${currentPromiseCount}) Promise started (<small>Async code started</small>)<br/>`
    );

    // Simulate asynchronous behavior with setTimeout
    window.setTimeout(() => {
      resolve(currentPromiseCount); // Fulfil the promise with the current count
    }, Math.random() * 2000 + 1000); // Wait between 1s and 3s
  });

  // Consume the promise
  p1.then((val) => {
    // Log the fulfilment value when the promise is resolved
    log.insertAdjacentHTML(
      "beforeend",
      `${val}) Promise fulfilled (<small>Async code terminated</small>)<br/>`
    );
  }).catch((reason) => {
    // Log the rejection reason if the promise is rejected
    console.log(`Handle rejected promise (${reason}) here.`);
  });

  // Indicate that the promise has been made, adding this message as the last child
  log.insertAdjacentHTML(
    "beforeend",
    `${currentPromiseCount}) Promise made (<small>Sync code terminated</small>)<br/>`
  );
}

// Check if the Promise feature is supported
if ("Promise" in window) {
  const btn = document.getElementById("btn");
  btn.addEventListener("click", testPromise); // Attach event listener to button
} else {
  const log = document.getElementById("log");
  log.innerHTML =
    "Live example not available as your browser doesn't support the <code>Promise</code> interface.";
}
