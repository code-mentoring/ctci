const isUnique = function (inputString) {
  const charSet = new Set(inputString.split(""));
  return inputString.length === charSet.size;
};

module.exports = { isUnique };
