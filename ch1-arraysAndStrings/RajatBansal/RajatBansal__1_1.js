/**1.1 - Is Unique
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? */

//with data structure
const isUnique = (str) => {
  if (str.length <= 1) {
    return true;
  }

  str = str.trim().toLowerCase(); //remove trailing and leading whitespaces if any

  const uniqueTracker = {}; //using object as the data structure
  /**
   * abcb => false
   * {
   *  a: 1,
   *  b: 2,
   *  c: 1,
   *  0: 1
   * }
   *
   * '0'
   */
  for (let letter of str) {
    if (uniqueTracker[letter]) {
      return false
    }
    else {
      uniqueTracker[letter] = 1;
    }
  }
  return true;
};

const isUniqueWithSet = str => {
  const strSet = new Set();
  str = str.trim().toLowerCase();
  for (let character of str) {
    strSet.add(character);
  }
  return strSet.size === str.length;
}

//no additional data structure
const isUniqueNoDS = (str) => {
  if (str.length <= 1) {
    return true;
  }

  str = str.trim().toLowerCase();
  str = str.split("").sort();

  let previousCharacter = str[0];
  for (let i = 1; i < str.length; i++) {
    if (str[i] === previousCharacter) {
      return false;
    } else {
      previousCharacter = str[i];
    }
  }
  return true;
};

//tests
const testStrings = [
  "a", //true
  "helloworld", //false
  "heloword1122", //false
  "abcdef1234", //true
  "  abcdef1234  ", //true
  "  _abcdef1234__  ", //false
  "abc0", //true
];

console.log("Testing below strings with isUnique method");
for (let testString of testStrings) {
  console.log(`Is '${testString}' unique? `, isUnique(testString));
}

console.log("-------------------------------------------");

console.log("Testing below strings with isUniqueWithSet method");
for (let testString of testStrings) {
  console.log(`Is '${testString}' unique? `, isUniqueWithSet(testString));
}

console.log("-------------------------------------------");

console.log("Testing below strings with isUniqueNoDS method");
for (let testString of testStrings) {
  console.log(`Is '${testString}' unique? `, isUniqueNoDS(testString));
}
