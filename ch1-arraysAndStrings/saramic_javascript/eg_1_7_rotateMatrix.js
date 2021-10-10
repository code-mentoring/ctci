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

const rotateMatrixInplace = function (matrix) {
  if (matrix.length < 1) return matrix;

  const maxCol = matrix[0].length - 1;
  const maxRow = matrix.length - 1;

  for (let row = 0; row < maxRow / 2; row++) {
    for (let col = 0; col <= maxCol / 2; col++) {
      const swap = matrix[row][col];
      matrix[row][col] = matrix[maxCol - col][row];
      matrix[maxCol - col][row] = matrix[maxRow - row][maxCol - col];
      matrix[maxRow - row][maxCol - col] = matrix[col][maxRow - row];
      matrix[col][maxRow - row] = swap;
    }
  }
  return matrix;
};

module.exports = { rotateMatrix, rotateMatrixInplace };
