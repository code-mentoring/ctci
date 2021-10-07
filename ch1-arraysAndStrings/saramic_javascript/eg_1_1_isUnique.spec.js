const { isUnique } = require("./eg_1_1_isUnique");

// 1.1 - Is Unique
// Implement an algorithm to determine if a string has all unique characters.
// What if you cannot use additional data structures?
describe("IsUnique", () => {
  it("empty string has unique characters", () => {
    expect(isUnique("")).toBeTruthy();
  });

  it("alphabetical string has unique characters", () => {
    expect(isUnique("abc")).toBeTruthy();
  });

  it("duplicate character does NOT have unique characters", () => {
    expect(isUnique("aabc")).toBeFalsy();
  });

  it("mixed case alphabetical string has unique characters", () => {
    expect(isUnique("aAbBcC")).toBeTruthy();
  });
});
