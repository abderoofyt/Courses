let total = 0;

function add(){
	// Increment total by 10 each time the function is called.
	total += 10;
	alert(total);
	
	/* 
	Store the updated total in sessionStorage so it can be accessed across pages
	during the same session.

	sessionStorage persists data as long as the browser tab is open, 
	but it will be cleared when the tab is closed. 
	*/
	sessionStorage.setItem("total", total);
}

function showUs(){
	// Retrieve the stored total from sessionStorage.
	// This allows us to access the value of total even after navigating to a
	// different page within the session.
	alert(sessionStorage.getItem("total"));
}
