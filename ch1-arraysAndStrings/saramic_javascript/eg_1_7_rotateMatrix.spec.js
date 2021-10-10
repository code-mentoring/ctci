const { rotateMatrix, rotateMatrixInplace } = require("./eg_1_7_rotateMatrix");

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

  describe("rotateMatrixInplace", () => {
    it("rotates an empty matrix", () => {
      expect(rotateMatrixInplace([])).toEqual([]);
    });

    it("rotates a 1 by 1 matrix", () => {
      expect(rotateMatrixInplace([[1]])).toEqual([[1]]);
    });

    describe("for a 3 by 3 matrix", () => {
      let matrix3x3 = [];
      beforeEach(() => {
        matrix3x3 = [
          [1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
        ];
      });

      it("moves top left to top right", () => {
        expect(rotateMatrixInplace(matrix3x3)[0][2]).toEqual(1);
      });

      it("moves top right to bottom right", () => {
        expect(rotateMatrixInplace(matrix3x3)[2][2]).toEqual(3);
      });

      it("moves bottom right to bottom left", () => {
        expect(rotateMatrixInplace(matrix3x3)[2][0]).toEqual(9);
      });

      it("moves bottom left to top left", () => {
        expect(rotateMatrixInplace(matrix3x3)[0][0]).toEqual(7);
      });

      it("moves center top to center right", () => {
        expect(rotateMatrixInplace(matrix3x3)[1][2]).toEqual(2);
      });

      it("moves center right to center bottom", () => {
        expect(rotateMatrixInplace(matrix3x3)[2][1]).toEqual(6);
      });

      it("rotates a 3 by 3 matrix", () => {
        expect(rotateMatrixInplace(matrix3x3)).toEqual([
          [7, 4, 1],
          [8, 5, 2],
          [9, 6, 3],
        ]);
      });
    });

    describe("for an even dimension square matrix", () => {
      let matrix4x4 = [];
      beforeEach(() => {
        matrix4x4 = [
          [1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
        ];
      });

      it("first row becomes last column", () => {
        expect(
          rotateMatrixInplace(matrix4x4).map((row) => row[row.length - 1])
        ).toEqual([1, 2, 3, 4]);
      });

      it("second row becomes second last column", () => {
        expect(
          rotateMatrixInplace(matrix4x4).map((row) => row[row.length - 2])
        ).toEqual([5, 6, 7, 8]);
      });

      it("third row becomes third last column", () => {
        expect(
          rotateMatrixInplace(matrix4x4).map((row) => row[row.length - 3])
        ).toEqual([9, 10, 11, 12]);
      });

      it("last row becomes first column", () => {
        expect(rotateMatrixInplace(matrix4x4).map((row) => row[0])).toEqual([
          13, 14, 15, 16,
        ]);
      });
    });
  });
});
