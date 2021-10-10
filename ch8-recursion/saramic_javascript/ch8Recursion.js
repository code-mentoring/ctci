const tripleSet = () => {};
const robotPath = () => {};

const basicMagicIndex = (sortedArray, options = {}) => {
  let tick = 0;
  const result = sortedArray.find((value, index) => {
    if (options.tick) tick++;
    return value === index;
  });
  if (options.tick) {
    return [result, tick];
  }
  return result;
};

const magicIndex = (
  sortedArray,
  tick = false,
  count = 0,
  base = 0,
  max = undefined
) => {
  if (!sortedArray) return tick ? [undefined, count] : undefined;
  if (!max) max = sortedArray.length;

  const halfIndex = Math.ceil(sortedArray.length / 2);
  const newBase = base + halfIndex;

  if (sortedArray[halfIndex] < newBase) {
    return magicIndex(
      sortedArray.slice(halfIndex),
      tick,
      count + 1,
      newBase,
      max
    );
  } else if (sortedArray[halfIndex] > newBase) {
    return magicIndex(
      sortedArray.slice(0, halfIndex),
      tick,
      count + 1,
      base,
      max
    );
  }

  return tick ? [newBase, count] : newBase;
};

const powerSet = () => {};

module.exports = {
  tripleSet,
  robotPath,
  basicMagicIndex,
  magicIndex,
  powerSet,
};
