function checkUnique(inputString) {
  if(inputString) {
    const convertedString = inputString.toString();
    const uniqueChars = new Set(convertedString);
    if(convertedString.length == Array.from(uniqueChars.values()).length) return true;
  };
  
  return false;
};

function checkUniqueNoStruct(inputString) {
  if(!inputString) return false
  
  const convertedStr = inputString.toString();
  const convertedStrLen = convertedStr.length;

  for (let i = 0; i < convertedStrLen; i++) {
    for (let j = 0; j < convertedStrLen; j++) {
      if(i == j) continue;
      if(convertedStr[i] == convertedStr[j]) return false;
    }
  }

  return true
}

console.log(checkUnique("aeiou"), checkUniqueNoStruct("aeiou"));
console.log(checkUnique("banana"), checkUniqueNoStruct("banana"));
console.log(checkUnique("exit123"), checkUniqueNoStruct("exit123"));
console.log(checkUnique("cake22"), checkUniqueNoStruct("cake22"));
console.log(checkUnique("!@#*%()"), checkUniqueNoStruct("!@#*%()"));
console.log(checkUnique("!!@#("), checkUniqueNoStruct("!!@#("));
console.log(checkUnique(null), checkUniqueNoStruct(null));
console.log(checkUnique(undefined), checkUniqueNoStruct(undefined));
console.log(checkUnique(55), checkUniqueNoStruct(55));
console.log(checkUnique(123456), checkUniqueNoStruct(123456));
