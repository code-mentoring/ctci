function checkUnique(inputString) {
  if(inputString) {
    const convertedString = inputString.toString();
    const uniqueChars = new Set(convertedString);
    if(convertedString.length == Array.from(uniqueChars.values()).length) return true;
  };
  
  return false;
};

function checkUniqueNoStruct(inputString) {
  if(inputString) {
    const convertedStr = inputString.toString();
    const convertedStrLen = convertedStr.length;

    for (let i = 0; i < convertedStrLen; i++) {
      for (let j = 0; j < convertedStrLen; j++) {
        if(i == j) continue;
        if(convertedStr[i] == convertedStr[j]) return false;
      }
    }
  }

  return true
}

console.log(checkUnique("aeiou"));
console.log(checkUnique("banana"));
console.log(checkUnique("exit123"));
console.log(checkUnique("cake22"));
console.log(checkUnique("!@#*%()"));
console.log(checkUnique("!!@#("));
console.log(checkUnique(null));
console.log(checkUnique(undefined));
console.log(checkUnique(55));
console.log(checkUnique(123456));

console.log(checkUniqueNoStruct("aeiou"));
console.log(checkUniqueNoStruct("banana"));
console.log(checkUniqueNoStruct("exit123"));
console.log(checkUniqueNoStruct("cake22"));
console.log(checkUniqueNoStruct("!@#*%()"));
console.log(checkUniqueNoStruct("!!@#("));
console.log(checkUniqueNoStruct(null));
console.log(checkUniqueNoStruct(undefined));
console.log(checkUniqueNoStruct(55));
console.log(checkUniqueNoStruct(123456));
