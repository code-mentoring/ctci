const tripleSet = () => {};
const robotPath = () => {};

const magicIndex = (sortedArray, options = {}) => {
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

const powerSet = () => {};

module.exports = { tripleSet, robotPath, magicIndex, powerSet };
