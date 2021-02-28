/**
 * Given an m x n matrix. If an element is 0, set its entire row and column to 0. 
 * 
 * Example1: 
 * Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 */

const setZeroMatrix = (matrixArr) => {
  const rowSet = new Set();
  const colSet = new Set();

  const rows = matrixArr.length;
  const cols = matrixArr[0].length;

  //go through the entire matrix and track row and column of all zeros, push them to row and col set
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (matrixArr[i][j] === 0) {
        rowSet.add(i);
        colSet.add(j);
      }
    }
  }

  //go through matrix again and if either row or column index is in set, set the element to 0
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      if (rowSet.has(i) || colSet.has(j)) {
        matrixArr[i][j] = 0;
      }
    }
  }

  return matrixArr;
};

console.log(
  setZeroMatrix([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
  ])
); //[[1,0,1],[0,0,0],[1,0,1]]

console.log(
  setZeroMatrix([
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5],
  ])
); //[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
