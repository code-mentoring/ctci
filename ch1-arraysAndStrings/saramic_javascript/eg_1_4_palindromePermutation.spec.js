const { palindromePermutation } = require("./eg_1_4_palindromePermutation");

// 1.4 - Palindrome Permutation
// Given a string, write a function to check if it is a permutation of a
// palindrome. A palindrome is a word or phrase that is the same forwards and
// backwards. A permutation is a rearrangement of letters. The palindrome does
// not need to be limited to just dictionary words.
//
// Given a string, determine if a permutation of the string could form a
// palindrome.
describe("palindromePermutation", () => {
  it("code can NOT form a palindrome", () => {
    expect(palindromePermutation("code")).toBeFalsy();
  });

  it("aab can form a palindrome", () => {
    expect(palindromePermutation("aab")).toBeTruthy();
  });

  it("carerac can form a palindrome", () => {
    expect(palindromePermutation("carerac")).toBeTruthy();
  });

  it("examples that CAN form a palindrome", () => {
    expect(palindromePermutation("aertyaert")).toBeTruthy();
    expect(palindromePermutation("123y321")).toBeTruthy();
    expect(palindromePermutation("Borrow or rob")).toBeTruthy();
    expect(palindromePermutation("A nut for a jar of tuna")).toBeTruthy();
    expect(palindromePermutation(123454321)).toBeTruthy();
    expect(palindromePermutation("aaacc")).toBeTruthy();
  });

  it("examples that CAN NOT form a palindrome", () => {
    expect(palindromePermutation("!@#$%^&*()")).toBeFalsy();
    expect(palindromePermutation(null)).toBeFalsy();
    expect(palindromePermutation(undefined)).toBeFalsy();
    expect(palindromePermutation(122213)).toBeFalsy();
    expect(palindromePermutation("aaaccc")).toBeFalsy();
  });
});
