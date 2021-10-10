const {
  tripleSet,
  robotPath,
  magicIndex,
  powerSet,
} = require("./ch8Recursion");

const logInputOutput = (funcToCall, input) => {
  const inputString = JSON.stringify(input);
  console.log(
    "input: ",
    inputString.padEnd(30 - inputString.split().length, " "),
    ` ${funcToCall.name}: `,
    JSON.stringify(funcToCall(input))
  );
};

let input;
console.log("8.1: Triple Step");
console.log("TODO ...");

console.log("\n8.2: Robot in a Grid");
console.log("TODO ...");

console.log("\n8.3: Magic Index");
input = [-1, 0, 2, 35];
logInputOutput(magicIndex, input);
input = [1, 2, 3, 4, 5];
logInputOutput(magicIndex, input);
input = [-1, 0, 1, 2, 3, 4, 5, 6, 7, 9, 11];
logInputOutput(magicIndex, input);
console.log(
  "Performed in: ",
  magicIndex(input, { tick: true })[1],
  " iterations"
);

console.log("\n8.4: Power Set");
console.log("TODO ...");
