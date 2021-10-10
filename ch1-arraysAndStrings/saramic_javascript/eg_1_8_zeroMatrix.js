const indexWithZeroFor = (matrix) =>
  matrix.reduce(
    (result, row, rowIndex) => [
      ...result,
      ...row
        .map((value, colIndex) => value === 0 && [rowIndex, colIndex])
        .filter((e) => e),
    ],
    []
  );

const zeroMatrix = function (matrix) {
  const withZero = indexWithZeroFor(matrix);
  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      withZero.forEach(
        ([rowIndex, colIndex]) =>
          (rowIndex === row || colIndex === col) && (matrix[row][col] = 0)
      );
    }
  }
  return matrix;
};

module.exports = { zeroMatrix };
