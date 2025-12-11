// 1. Defining some variables
const userName = "Learner";
const currentYear = 2025;
const birthYear = 1990;

// 2. Using console.log() to check values and logic
console.log("--- START of script.js execution ---");

// Check the value of userName
console.log("The user name is:", userName); 

// Perform a calculation and log the result
const age = currentYear - birthYear;
console.log("Calculated Age:", age); 

// 3. Interacting with the webpage (DOM Manipulation)
const element = document.getElementById('output-message');

if (element) {
    element.textContent = `Hello, ${userName}! You are approximately ${age} years old.`;
    
    // Log success to the console
    console.log("Successfully updated the paragraph text on the page.");
} else {
    // Log an error if the element wasn't found
    console.error("Error: Could not find the paragraph element with id 'output-message'.");
}

console.log("--- END of script.js execution ---");