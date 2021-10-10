const { checkPermutation } = require("./eg_1_2_checkPermutation");

// 1.2 - Check Permutation
// Given two strings, write a method to decide if one is a permutation of the
// other.
describe("checkPermutation", () => {
  it("asdf is a permutation of fdsa", () => {
    expect(checkPermutation("asdf", "fdsa")).toBeTruthy();
  });

  it("cat is NOT a permutation of dog", () => {
    expect(checkPermutation("cat", "dog")).toBeFalsy();
  });

  it("numeric 1234 is a permutation of 4321", () => {
    expect(checkPermutation(1234, 4321)).toBeTruthy();
  });

  it("1234 is NOT a permutation of 5678", () => {
    expect(checkPermutation(1234, 5678)).toBeFalsy();
  });

  it("null is a permutation of null", () => {
    expect(checkPermutation(null, null)).toBeTruthy();
  });

  it("undefined is a permutation of undefined", () => {
    expect(checkPermutation(undefined, undefined)).toBeTruthy();
  });
});
