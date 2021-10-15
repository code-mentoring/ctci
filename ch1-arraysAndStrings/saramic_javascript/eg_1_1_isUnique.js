const isUnique = function (inputString) {
  const inputChars = [...inputString]; // NOTE: spread on multi-byte characters
  const charSet = new Set(inputChars);
  return inputChars.length === charSet.size;
};

module.exports = { isUnique };
