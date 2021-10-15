const accumulateSameElement = (prev, element) =>
  !prev.lastElement || prev.lastElement === element
    ? {
        compressedString: prev.compressedString,
        lastElement: element,
        elementCount: prev.elementCount + 1,
      }
    : {
        compressedString:
          prev.compressedString + prev.lastElement + prev.elementCount,
        lastElement: element,
        elementCount: 1,
      };

const stringCompression = function (inputString) {
  const compressionHash = [...inputString].reduce(
    (prev, element) => accumulateSameElement(prev, element),
    { compressedString: "", lastElement: null, elementCount: 0 }
  );
  const compressedString =
    compressionHash.compressedString +
    compressionHash.lastElement +
    compressionHash.elementCount;

  return compressedString.length < inputString.length
    ? compressedString
    : inputString;
};

module.exports = { stringCompression };
