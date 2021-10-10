const valueToSortedChars = (value) =>
  value ? [...value.toString()].sort().join() : value;

const checkPermutation = function (input1, input2) {
  return valueToSortedChars(input1) === valueToSortedChars(input2);
};

module.exports = { checkPermutation };
