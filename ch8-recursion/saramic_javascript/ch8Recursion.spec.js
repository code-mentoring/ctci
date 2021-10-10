const {
  tripleSet,
  robotPath,
  basicMagicIndex,
  magicIndex,
  powerSet,
} = require("./ch8Recursion");

// # Chapter 8: Recursion and Dynamic Programming

// ## 8.1: Triple Step
// A child is running up a staircase with n steps and can hop either 1
// step, 2 steps, or 3 steps at a time. Implement a method to count how
// many possible ways the child can run up the stairs.
describe("tripleSet", () => {});

// ## 8.2 Robot in a Grid
// Imagine a robot sitting on the upper left corner of grid with r rows and
// c columns. The robot can only move in two directions, right and down, but
// certain cells are "off limits" such that the robot cannot step on them.
// Design an algorithm to find a path for the robot from the top left to the
// bottom right.
describe("robotPath", () => {});

// ## 8.3 Magic Index
// A magic index in an array A[e... n-1] is defined to be an index such that
// A[i] = i. Given a sorted array of distinct integers, write a method to find
// a magic index, if one exists, in array A.
// FOLLOW UP: What if the values are not distinct?
describe("magicIndex", () => {
  it("returns undefined if there is no magic index", () => {
    let input = [1, 2, 3, 4, 5];
    expect(basicMagicIndex(input)).toEqual(undefined);
    expect(magicIndex()).toEqual(undefined);
  });

  it("returns the magic index", () => {
    let input = [-200, -100, 2, 300, 400];
    expect(basicMagicIndex(input)).toEqual(2);
    expect(magicIndex(input)).toEqual(2);
  });

  it("returns one of the magic indices", () => {
    let input = [-200, -100, 2, 3, 400];
    expect(basicMagicIndex(input).toString()).toMatch(/^(2|3)$/);
    expect(magicIndex(input).toString()).toMatch(/^(2|3)$/);
  });

  describe("a large enough input array", () => {
    const elementIndex = 10000;
    const input = [
      ...Array(elementIndex)
        .fill(0)
        .map((e, i) => i - 1),
      elementIndex,
      ...Array(10000000)
        .fill(0)
        .map((e, i) => elementIndex + 2 + i),
    ];

    it("find the magic index in FAST O(log(n)) time (21 ticks)", () => {
      expect(magicIndex(input, { tick: true })).toEqual([elementIndex, 21]);
    });

    it("find the magic index in SLOW O(n) time (10,0001 ticks)", () => {
      expect(basicMagicIndex(input, { tick: true })).toEqual([
        elementIndex,
        10001,
      ]);
    });
  });
});

// ## 8.4 Power Set
// Write a method to return all subsets of a set.
describe("powerSet", () => {});
