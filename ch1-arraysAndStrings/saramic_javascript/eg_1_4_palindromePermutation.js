const palindromePermutation = function (input) {
  if (!input) return false;

  const charSet = new Set();
  [...input.toString()]
    .map((element) => element.toLowerCase())
    .forEach((element) => {
      charSet.has(element) ? charSet.delete(element) : charSet.add(element);
    });
  return charSet.size <= 1;
};

module.exports = { palindromePermutation };
