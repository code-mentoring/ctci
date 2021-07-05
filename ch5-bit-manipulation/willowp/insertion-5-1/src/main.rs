use num_traits::pow;

// Insert m into n, between bits j and i.
// Invar: n is larger than m.
// Invar: j - i == the number of used bits in m.
// Example:
// n = 0b10000100010
// m = 0b10011
// i = 2
// j = 6
// answer = 0b10001001110
fn insertion(n: i32, m: i32, i: i8, j: i8) -> i32 {
    // Build a mask of 1s with 0s where m will be inserted.
    // Important: 2**x - 1 fills a binary number with 1s up to index i.
    // Example: i = 2, j = 6, mask = 0b11111...10000011
    // Right side of mask is 0b11
    let right = pow(2, i as usize) - 1;
    // Left side of mask is 0b111111111111...10000000;
    let left = !(pow(2, (j + 1) as usize) - 1);
    let mask = left | right;
    let masked = n & mask;
    // Left-shift m to prepare for insertion.
    // Example 0b10011 << 2 = 0b1001100
    println!("{:#b}", -1);
    let shifted = m << i;
    // We now have:
    // 0b1...10000011
    // 0b0...01001100
    masked | shifted
}

fn main() {
    let n = 0b10000100010;
    let m = 0b10011;
    let i = 2;
    let j = 6;
    let expected = 0b10001001110;
    let received = insertion(n, m, i, j);
    assert_eq!(received, expected);
    println!("expected: {:b}", expected);
    println!("received: {:b}", received);
}
