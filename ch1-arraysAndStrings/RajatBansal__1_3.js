/**
 * 1.4 - Palindrome Permutation
Given a string, write a function to check if it is a permutation of a palindrome. 
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words. 
 */

const isPermutationPalindrome = (str) => {
  str = str.trim().toLowerCase();
  if (str.length <= 1) {
    return true;
  }

  let charTracker = {};

  for (let character of str) {
    charTracker[character] = charTracker[character]
      ? charTracker[character] + 1
      : 1;
  }

  //if all even its a palindrome combo
  //if one odd and rest even then also palindrome combo
  let oddCount = 0;
  for (let character in charTracker) {
    if (charTracker[character] % 2 !== 0) {
      oddCount += 1;
      //odd count exceeded
      if (oddCount > 1) {
        return false;
      }
    }
  }

  return true;
};

const testStrings = ["", "a", "ab", "abc", "  abba  ", "Racecar", "radar", "redder"];
console.log("Are following strings having permutation palindromes?");
for (let testString of testStrings) {
  console.log(`${testString}: ${isPermutationPalindrome(testString)}`);
}
