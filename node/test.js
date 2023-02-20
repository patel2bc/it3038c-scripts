const path = require("path");
const hello = "Hello from Node JS Variable!"
console.log(hello)

console.log(`Printing variable hello: ${hello}`);
console.log("dir name: " + __dirname);
console.log("dir and file name: " + __filename);

console.log("Using PATH module:");
console.log(`Hello from file ${path.basename(__filename)}`);

console.log(`Process args: ${process.argv}`)