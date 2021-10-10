console.log("Session 1.1 - isUnique");
const { isUnique } = require("./eg_1_1_isUnique");
const logInputOutput = (functionName, input, output) => {
  const inputString = JSON.stringify(input);
  console.log(
    "input: ",
    inputString.padEnd(20 - inputString.split().length, " "),
    ` ${functionName}: `,
    JSON.stringify(output)
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

console.log("\nSession 1.6 - stringCompression");
const { stringCompression } = require("./eg_1_6_stringCompression");
["aabcccccaaa", "aabbcc", "aaaaaaaaaaaaaaa"].forEach((input) =>
  logInputOutput("stringCompression", input, stringCompression(input))
);

console.log("\nSession 1.7 - rotateMatrix");
const { rotateMatrix, rotateMatrixInplace } = require("./eg_1_7_rotateMatrix");
const logMatrix = (matrix) =>
  `[\n${matrix.map((row) => `  ${row}`).join("\n")}\n]`;
const logInputOutputMatrix = (input, output) => {
  console.log(
    "input: ",
    logMatrix(input),
    "\noutput: ",
    logMatrix(output),
    "\n"
  );
};

let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
logInputOutputMatrix(matrix, rotateMatrix(matrix));

matrix = [
  [1, 2, 3],
  [4, 5, 6],
];
logInputOutputMatrix(matrix, rotateMatrix(matrix));

console.log("rotate matrix in place");
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];
console.log(logMatrix(matrix));
console.log(logMatrix(rotateMatrixInplace(matrix)));

matrix = [
  [0, 1, 2, 3, 4],
  [1, 2, 3, 4, 5],
  [2, 3, 4, 5, 6],
  [3, 4, 5, 6, 7],
  [4, 5, 6, 7, 8],
];
console.log(logMatrix(matrix));
console.log(logMatrix(rotateMatrixInplace(matrix)));
