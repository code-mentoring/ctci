'use strict';

// Zero matrix: Write an algorithm such that is an element in an MxN matrix is 0,
//it's entire row and column are set to 0. 

let arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 0, 8],
    [9, 10, 11]
];

function zeroMatrix(matrix) {
    let x = 0;
    let y = 0;
    for (let i = 0; i < matrix.length; i++) {
        for (let j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] === 0) {
                x = i;
                y = j;

            }
        }
    }

    // console.log(x)
    // console.log(y)
    let newMatrix = matrix;
    for (let k = 0; k < matrix.length; k++) {
        for (let l = 0; l < matrix[0].length; l++) {
            if (k === x || l === y) {
                newMatrix[k][l] = 0;
            }
        }
    }
    return newMatrix;
}

// console.log(zeroMatrix(arr))

//test
let myArr = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [0, 2, 3, 4, 5]
];

console.log(zeroMatrix(myArr))
