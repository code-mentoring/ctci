console.log("Session 1.1 - isUnique");
const { isUnique } = require("./eg_1_1_isUnique");
const logIsUnique = (input) => {
  console.log(
    "input: ",
    JSON.stringify(input).padEnd(10 - input.split().length, " "),
    " isUnique: ",
    isUnique(input)
  );
};
logIsUnique("");
logIsUnique("abc");
logIsUnique("aabc");
logIsUnique("\t\t");
logIsUnique("😀😀");
logIsUnique("😀🙁");
