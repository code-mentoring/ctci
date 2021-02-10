/**1.1 - Is Unique
Implement an algorithm to determine if a string has all unique characters. What if you
cannot use additional data structures? */

const isUnique = str => {

  if (str.length <= 1) {
    return true;
  }

  str = str.trim(); //remove trailing and leading whitespaces if any

  const uniqueTracker = {};

  for (let letter of str) {
    uniqueTracker[letter] = uniqueTracker[letter] ? uniqueTracker[letter] + 1 : 1;
  }

  for (let letter in uniqueTracker) {
    if (uniqueTracker[letter] > 1) {
      return false;
    }
  }

  return true;
}


//tests
console.log(isUnique('helloworld')); //false
console.log(isUnique('abcdef1234')); //true
console.log(isUnique('  abcdef1234  ')); //true
console.log(isUnique('  _abcdef1234__  ')); //false
