/**1.1 - Is Unique
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? */

const isUnique = (str) => {
  if (str.length <= 1) {
    return true;
  }

  str = str.trim(); //remove trailing and leading whitespaces if any

  const uniqueTracker = {};

  for (let letter of str) {
    uniqueTracker[letter] = uniqueTracker[letter]
      ? uniqueTracker[letter] + 1
      : 1;
  }

  for (let letter in uniqueTracker) {
    if (uniqueTracker[letter] > 1) {
      return false;
    }
  }

  return true;
};

//no additional data structure
const isUniqueNoDS = (str) => {
  if (str.length <= 1) {
    return true;
  }

  str = str.trim();
  str = str.split("").sort();

  let firstCharacter = str[0];
  for (let i = 1; i < str.length; i++) {
    if (str[i] === firstCharacter) {
      return false;
    } else {
      firstCharacter = str[i];
    }
  }
  return true;
};

//tests
const testStrings = [
  "a",
  "helloworld",
  "heloword1122",
  "abcdef1234",
  "  abcdef1234  ",
  "  _abcdef1234__  ",
];

console.log("Testing below strings with isUnique method");
for (let testString of testStrings) {
  console.log(`Is '${testString}' unique? `, isUnique(testString));
}

console.log("-------------------------------------------");

console.log("Testing below strings with isUniqueNoDS method");
for (let testString of testStrings) {
  console.log(`Is '${testString}' unique? `, isUniqueNoDS(testString));
}
