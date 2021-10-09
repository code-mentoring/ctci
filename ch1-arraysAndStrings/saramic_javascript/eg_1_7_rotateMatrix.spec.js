const { rotateMatrix } = require("./eg_1_7_rotateMatrix");

// 1.7 - Rotate Matrix:
// Given an image represented by an NxN matrix, where each pixel in the image
// is an integer, write a method to rotate the image by 90 degrees. Can you do
// this in place?
describe("rotateMatrix", () => {
  it("rotates an empty matrix", () => {
    expect(rotateMatrix([])).toEqual([]);
  });

  it("rotates a 1 by 1 matrix", () => {
    expect(rotateMatrix([[1]])).toEqual([[1]]);
  });

  it("rotates a 2 by 1 matrix", () => {
    expect(rotateMatrix([[1, 2]])).toEqual([[1], [2]]);
  });

  it("rotates a 1 by 2 matrix", () => {
    expect(rotateMatrix([[1], [2]])).toEqual([[2, 1]]);
  });

  it("rotates a 3 by 2 matrix", () => {
    expect(
      rotateMatrix([
        [1, 2, 3],
        [4, 5, 6],
      ])
    ).toEqual([
      [4, 1],
      [5, 2],
      [6, 3],
    ]);
  });
});
