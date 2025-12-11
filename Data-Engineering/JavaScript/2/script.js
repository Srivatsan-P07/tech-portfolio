// Constant

const PI = 3.14
console.log("Value of PI:", PI);

// PI = 2 --> Error

// ---------------------------------------------

// Let (Changing values)

let radius = 5;
console.log('Initial Radius:', radius);

radius = 10;
radius = radius + 5;
console.log('Updated Radius:', radius);

// let radius = 20; // Error: Identifier 'radius' has already been declared

// ---------------------------------------------

// Var (Function scoped)

var height = 15;
console.log('Initial Height:', height);

height = 25;
console.log('Updated Height:', height);

var height = null; // No Error
console.log('Redeclared Height:', height);


// ---------------------------------------------
let address;
console.log('Address:', address); // undefined
