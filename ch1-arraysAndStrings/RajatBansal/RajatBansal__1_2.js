/**1.2 - Check Permutation
Given two strings, write a method to decide if one is a permutation of the
other. */

const isPermutation = (str1, str2) => {
  str1 = str1.trim().toLowerCase();
  str2 = str2.trim().toLowerCase();

  //corner cases
  if (!str1.length && !str2.length) {
    //both 0 or null
    return true;
  } else if (str1.length !== str2.length) {
    return false;
  } else if (str1.length === 1 && str2.length === 1) {
    return str1 === str2;
  }

  const strTracker = {};
  for (let character of str1) {
    strTracker[character] = strTracker[character]
      ? strTracker[character] + 1
      : 1;
  }

  for (let character of str2) {
    if (strTracker[character]) {
      strTracker[character] -= 1;
    } else {
      return false;
    }
  }

  for (let character in strTracker) {
    if (strTracker[character] !== 0) {
      return false;
    }
  }

  return true;
};

const testStrings = [
  ["", ""], //true
  ["a", "b"], //false
  ["c", "c"], //true
  ["  abcd ", " abce "], //false
  ["abc123", "12abc3"], //true
  ["godly love", "lovely god"],
];
console.log("Are following 2 strings combos?");

for (let stringCombo of testStrings) {
  const firstStr = stringCombo[0];
  const secondStr = stringCombo[1];
  console.log(
    `${firstStr}, ${secondStr}: ${isPermutation(firstStr, secondStr)}`
  );
}

