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

  describe("multi width and similar characters", () => {
    it("a string with unique emoji has unique characters", () => {
      expect(isUnique("😀😃😄😁😆😅😂🤣")).toBeTruthy();
    });

    it("a string with duplicate same emoji does NOT have unique characters", () => {
      expect(isUnique("😀😀😃")).toBeFalsy();
    });

    it("a string with a space and tab character is unique", () => {
      expect(isUnique("spc tab	")).toBeTruthy();
    });

    it("a tab and a \\t are NOT unique", () => {
      expect(isUnique("	\t")).toBeFalsy();
    });

    it("2 new lines are NOT unique", () => {
      expect(isUnique("\n\n")).toBeFalsy();
    });
  });
});
