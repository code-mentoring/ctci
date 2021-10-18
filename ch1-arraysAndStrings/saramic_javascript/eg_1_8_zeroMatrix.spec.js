const { zeroMatrix } = require("./eg_1_8_zeroMatrix");

// 1.8 - Zero Matrix:
// Write an algorithm such that if an element in an MxN matrix is 0, its entire
// row and column are set to 0.
describe("zeroMatrix", () => {
  it("returns array unaltered if there are no 0 elements", () => {
    expect(
      zeroMatrix([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
      ])
    ).toEqual([
      [1, 1, 1],
      [1, 1, 1],
      [1, 1, 1],
    ]);
  });

  it("zeros out a whole column and row", () => {
    expect(
      zeroMatrix([
        [1, 1, 1],
        [1, 0, 0],
        [1, 1, 1],
      ])
    ).toEqual([
      [1, 0, 0],
      [0, 0, 0],
      [1, 0, 0],
    ]);
  });
});
