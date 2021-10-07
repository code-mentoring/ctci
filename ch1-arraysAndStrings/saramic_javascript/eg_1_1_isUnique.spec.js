const { isUnique } = require("./eg_1_1_isUnique");

// 1.1 - Is Unique
// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?
describe("IsUnique", () => {
  it("empty string has unique characters", () => {
    expect(isUnique("")).toBeTruthy();
  });
});
