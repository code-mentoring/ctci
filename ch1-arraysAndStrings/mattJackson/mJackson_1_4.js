/*
* Using Shane's hint. The theory is that if there is only one character that appears only once
* and the rest are even numbers, there exists a permutation that is a palindrome mirrored across
* the single char.
*/

function checkPalindrome(inputString) {
  if(!inputString) return false;
  const convertedString = inputString.toString().toLowerCase();
  map1 = makeMap(convertedString);
  let notEvenCount = 0;

  for (entry of map1.entries()) {
    if(entry[1] % 2 > 0) notEvenCount++;
    if (notEvenCount > 1) return false
  };
  
  return true;
};

function makeMap(string) {
  let newMap = new Map();

  Array.from(string).forEach(letter => {
    if(newMap.has(letter)) {
      newMap.set(letter, newMap.get(letter) + 1)
    } else {
      newMap.set(letter, 1);
    }
  })

  return newMap;
};

console.log(checkPalindrome("aertyaert"));
console.log(checkPalindrome("123y321"));
console.log(checkPalindrome("!@#$%^&*()"));
console.log(checkPalindrome(null));
console.log(checkPalindrome(undefined));
console.log(checkPalindrome("Borrow or rob"));
console.log(checkPalindrome("A nut for a jar of tuna"));
console.log(checkPalindrome(123454321));
console.log(checkPalindrome(122213));
console.log(checkPalindrome("aaaccc"));
console.log(checkPalindrome("aaacc"));
