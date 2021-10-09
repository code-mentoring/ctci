const rotateMatrix = function (matrix) {
  if (matrix.length < 1) return matrix;

  const colCount = matrix[0].length;
  const rowCount = matrix.length;

  const outputMatrix = Array(colCount)
    .fill(0)
    .map(() => Array(rowCount));

  matrix.forEach((row, rowIndex) => {
    row.forEach((value, colIndex) => {
      outputMatrix[colIndex][rowCount - 1 - rowIndex] = value;
    });
  });
  return outputMatrix;
};

module.exports = { rotateMatrix };
