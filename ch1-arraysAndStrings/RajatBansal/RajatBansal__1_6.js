/**
 * String Compression: Implement a method to perform basic string compression using the counts of repeated characters.
 * For example, the string a a b c c c c c a a a would become a 2 b l c 5 a 3.
 * If the "compressed" string would not become smaller than the original string, your method should return the original string.
 * You can assume the string has only uppercase and lowercase letters (a - z).
 */

const compressString = (str) => {
  str = str.trim();

  if (str.length <= 1) {
    return str;
  }

  let previousChar = str[0];
  let compressedStr = "";
  let charCount = 1;
  for (let i = 1; i < str.length; i++) {
    if (str[i] === previousChar) {
      charCount += 1;
    } else {
      compressedStr = compressedStr.concat(previousChar, charCount);
      previousChar = str[i];
      charCount = 1;
    }
  }
  //appending final values here
  compressedStr = compressedStr.concat(previousChar, charCount);

  if (compressedStr.length >= str.length) {
    return str;
  }

  return compressedStr;
};

const testStrings = [
  "",
  "a", //a
  "ab", //ab
  "abc", //abc
  "aaaccc", //a3c3
  "abbbcc", //abbbcc
  "abbbbbbbcc", //a1b3c2
  "aabcccccaaa", //a2b1c5a3
  "aaabbcccccdaaa", //a3b2c5d1a3
  "aabbbcdddddde", //a2b3c1d6e1
  "ABBBBBBbbbbbbcccDd", //A1B6b6c3D1d1
];
for (let testString of testStrings) {
  console.log(`${testString}: ${compressString(testString)}`);
}
