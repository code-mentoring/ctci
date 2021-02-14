function checkPerm(string1, string2) {
  if(!string1 || !string2) return false;
  map1 = makeMap(string1);
  map2 = makeMap(string2);

  for (entry of map1.entries()) {
    if(!map2.has(entry[0]) || map2.get(entry[0]) != entry[1]) return false;
  };
  
  return true;
}

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
}

console.log(checkPerm("doggy", "soggy"));
console.log(checkPerm("doggy", "odgyg"));
console.log(checkPerm(123141, 141321));
console.log(checkPerm("!@#!@#", 141321));
console.log(checkPerm("endows", "snowed"));
console.log(checkPerm(null, null));
