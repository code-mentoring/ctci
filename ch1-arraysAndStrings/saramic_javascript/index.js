console.log("Session 1.1 - isUnique");
const { isUnique } = require("./eg_1_1_isUnique");
let input = "";
console.log(
  "input:    ",
  JSON.stringify(input),
  "        isUnique: ",
  isUnique(input)
);
input = "abc";
console.log(
  "input:    ",
  JSON.stringify(input),
  "     isUnique: ",
  isUnique(input)
);
input = "aabc";
console.log(
  "input:    ",
  JSON.stringify(input),
  "    isUnique: ",
  isUnique(input)
);
