console.log("Session 1.1 - isUnique");
const { isUnique } = require("./eg_1_1_isUnique");
const logInputOutput = (functionName, input, output) => {
  const inputString = JSON.stringify(input);
  console.log(
    "input: ",
    inputString.padEnd(20 - inputString.split().length, " "),
    ` ${functionName}: `,
    output
  );
};
["", "abc", "aabc", "\t\t", "😀😀", "😀🙁"].forEach((input) =>
  logInputOutput("isUnique", input, isUnique(input))
);

console.log("\nSession 1.2 - checkPermutation");
const { checkPermutation } = require("./eg_1_2_checkPermutation");
[
  ["asdf", "fdsa"],
  ["sarah", "michael"],
  ["god", "dog"],
  [1234, 4321],
  [null, null],
  [null, undefined], // NOTE: undefined is rendered as null by JSON.stringify in logInputOutput
].forEach((input) =>
  logInputOutput("checkPermutation", input, checkPermutation(...input))
);

console.log("\nSession 1.4 - palindromePermutation");
const { palindromePermutation } = require("./eg_1_4_palindromePermutation");
[
  "code",
  "aab",
  "carerac",
  "Borrow or rob",
  123454321,
  "!@#$%^&*()",
  null,
].forEach((input) =>
  logInputOutput("palindromePermutation", input, palindromePermutation(input))
);
