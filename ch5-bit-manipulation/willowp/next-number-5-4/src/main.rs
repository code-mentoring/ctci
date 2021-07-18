// Next Number: Given a positive integer,
// print the next smallest and the next largest number
// that have the same number of 1 bits in their binary representation.

// Question - What if there isn't a smaller number with the same number of 1 bits?
// Could theoretically go to negative.
// 0 0000111 = 7
// 1 1100000 = 1 + 2 + 4 + 8 + 16 = -31
// This solution does not support this, and throws an error instead.

use num_traits::pow;

fn clear_bits_right(n: u32, i: u32) -> u32 {
    // Clear all bits to the right of an index.
    let mask = !(pow(2, (i - 1) as usize));
    n & mask
}

fn count_ones(n: u32, i:u32) -> u32 {
    // Count the number of ones to the right of a given index, including the index.
    let mut ones = get_bit(n, 0);
    let mut cur = 1;
    while cur <= i {
        if get_bit(n, cur) == 1 {
            ones += 1;
        }
        cur += 1;
    }
    ones
}

// Flip the bit at a given index.
fn flip_bit(n: u32, i: u32) -> u32 {
    n ^ (1 << i)
}

// Return the bit at a given index.
fn get_bit(num: u32, i: u32) -> u32 {
    num & (1 << i)
}

fn next_largest(n: u32) -> u32{
    // Find the first 0 that occurs after a 1.
    // Flip them both.
    // Move all 1s to the right of that as far right as possible.
    let target = next_zero(n, next_one(n, 0));
    let largest = flip_bit(flip_bit(n, target), target - 1);
    // We can only move 1s right if we have at least 2 bits.
    if target > 2 {
        // Mask of 1s
        let mask = pow(2, (count_ones(largest, target - 1) - 1) as usize);
        return mask | clear_bits_right(largest, target - 1);
    };
    largest
}

// Like next zero but finds the next 1.
fn next_one(n: u32, i: u32) -> u32 {
    let mut one = i;
    let mut mask = 1 << i;
    if n < pow(2, i as usize) {
        panic!("No 1 at an index >= to {} in {}. This number would return a negative value, which is not yet supported.", i, n);
    }
    while mask & n == 0 {
        mask = mask << 1;
        one += 1;
    }
    one
}

fn next_number(n: u32) -> [u32; 2] {
    if n == 0 || n == !0 {
        println!("Can't do anything with this.");
        return [n, n];
    }
    [next_smallest(n), next_largest(n)]
}

fn next_smallest(n: u32) -> u32 {
    // Find the first 1 that occurs after a 0.
    // Flip the 1 and the 0 next to it.
    let target = next_one(n, next_zero(n, 0));
    flip_bit(flip_bit(n, target), target - 1)
}

// Given a number and an index, return the index of the next 0 bit.
// Answer is INCLUSIVE of i.
// Example:
// n = 10(base 2), i = 0, returns 0
// n = 1011(base 2), i = 0, returns 2
// n = 1010(base 2), i = 1, returns 2
fn next_zero(n: u32, i: u32) -> u32 {
    let mut zero = i;
    let mut mask = 1 << i;
    while mask | n == n {
        mask = mask << 1;
        zero += 1;
    }
    zero
}

fn main() {
    let cases = [[
        0b11011,
        0b10111,
        0b11101,
        //11110
    ], [
        0b110,
        0b101,
        0b1001,
    ], [
        0b101010101010101,
        0b101010101010011,
        0b101010101010110,
    ],[
        0b1010,
        0b1001,
        0b1100,
    ], [
        0b1000110,
        0b1000101,
        0b1001001,
    ]];
    for c in cases {
        println!("Processing:      {:b}", c[0]);
        let res = next_number(c[0]);
        println!("Smallest:");
        println!("Expected:        {:b}", c[1]);
        println!("Received:        {:b}", res[0]);
        println!("Largest:");
        println!("Expected:        {:b}", c[2]);
        println!("Received:        {:b}", res[1]);
        println!("{:?}, {:?}", c, res);
    }
}
