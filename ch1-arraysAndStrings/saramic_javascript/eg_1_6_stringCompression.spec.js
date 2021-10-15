const { stringCompression } = require("./eg_1_6_stringCompression");

// 1.6 - String Compression:
// Implement a method to perform basic string compression using the counts of
// repeated characters. For example, the string a a b c c c c c a a a would
// become a 2 b l c 5 a 3 , If the "compressed" string would not become smaller
// than the original string, your method should return the original string. You
// can assume the string has only uppercase and lowercase letters (a - z).
describe("stringCompression", () => {
  it("compresses a string", () => {
    expect(stringCompression("aabcccccaaa")).toEqual("a2b1c5a3");
  });

  it("returns the string if it is the same length as the compression", () => {
    expect(stringCompression("aabbcc")).toEqual("aabbcc");
  });

  it("returns the string if it is shorter than the compression", () => {
    expect(stringCompression("aabbccdef")).toEqual("aabbccdef");
  });

  it("compresses strings appropriately", () => {
    expect(stringCompression("aaaaabbbbccc")).toEqual("a5b4c3");
  });
});
