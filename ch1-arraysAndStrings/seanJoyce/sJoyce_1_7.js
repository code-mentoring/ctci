'use strict';

// Given an image represented by an NxN matrix,
// where each pixel in the image is an integer, 
// write a method to rotate the image by 90 degrees.
// Can you do this in place ?

let matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
];

rotateMatrix(matrix);

function rotateMatrix(matrix) {
    //init newMatrix
    let newMatrix = [];
    //loop through original matrix 
    for (let i = 0; i < matrix.length; i++) {
        //create new row array 
        let row = matrix.map((j) => (j[i])).reverse()

        //append new row to newMatrix
        newMatrix.push(row);
        break;
        // break;
    }
    console.log(newMatrix)
    return newMatrix;
}













