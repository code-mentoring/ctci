const {
  tripleSet,
  robotPath,
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
    expect(magicIndex([1, 2, 3, 4, 5])).toEqual(undefined);
  });

  it("returns the magic index", () => {
    expect(magicIndex([-200, -100, 2, 300, 400])).toEqual(2);
  });

  it("returns one of the magic indices", () => {
    expect(magicIndex([-200, -100, 2, 3, 400]).toString()).toMatch(/^(2|3)$/);
  });

  xit("find the magic index in log n time", () => {
    const elementIndex = 10000;
    const input = [
      ...Array(elementIndex)
        .fill(0)
        .map((e, i) => i - 1),
      elementIndex,
      ...Array(10000000)
        .fill(0)
        .map((e, i) => elementIndex + i),
    ];
    expect(magicIndex(input, { tick: true })).toEqual([elementIndex, 100]);
  });
});

// ## 8.4 Power Set
// Write a method to return all subsets of a set.
describe("powerSet", () => {});
