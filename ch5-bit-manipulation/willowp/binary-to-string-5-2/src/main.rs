// Print the representation of a number between 0 and 1 (inclusive) in binary.
// The answer will be similar to https://stackoverflow.com/a/34243735/15038439
// But assumes that the decimal is after the leftmost bit.
// float can be represented in 32 characters if it:
// a) terminates before 32 characters - ie 0.25 = 001
// b) repeats before 30 characters - ie 0.72 = (01011100001010001111)
// Examples:
// 1 == "1"
// 0 == "0"
// 0.625 == "0101"
// Repeating sequences are represented with brackets:
// 0.72  "(01011100001010001111)"
// 0.00625 == "0000000(0110)"
// If more than 32 bits are required, returns "ERROR":
// 0.000625 == "ERROR"
// NOTE: long decimals may not be handled correctly due to rounding errors.
// Example of processing:
// 0.72 - 0
// 1.44 - 1
// 0.88 - 0
// 1.76 - 1
// 1.52 - 1
// 1.04 - 1
// 0.08 - 0
// 0.16 - 0
// 0.32 - 0
// 0.64 - 0
// 1.28 - 1
// 0.56 - 0
// 1.12 - 1
// 0.24 - 0
// 0.48 - 0
// 0.96 - 0
// 1.92 - 1
// 1.84 - 1
// 1.68 - 1
// 1.36 - 1
// 0.72 - 0
fn binary_to_string(n: f32) -> String {
    if n == 1.0 {
        return "1".to_string();
    };
    // To avoid rounding errors, convert the float to an integer
    // multiplying by 10 until no more decimals exist.
    // Because of rounding errors in large decimals, this could produce an incorrect factor,
    // but that will likely result in ERROR anyway, since it will need more than 32 bits.
    let mut factor: u32 = 10;
    while (n * factor as f32).floor() != n * factor as f32 {
        factor *= 10;
    }
    // Handle leading zeroes.
    // If there are leading zeroes, keep track in case it repeats.
    // start will keep track of leading zeroes.
    let mut start = String::from("0");
    // first_one is the first case where multiplying it by 2 is greater than factor.
    // Ie, it is the number where the leading zeroes end.
    let mut first_one: u32 = 0;
    let mut rest = String::new();

    // Last time that `n` is referenced.
    // `cur` is the value currently being processed.
    let mut cur: u32 = (n * factor as f32) as u32;
    while start.len() + rest.len() < 32 {
        if cur == 0 {
            // Termination! Clean output.
            return start.to_owned() + &rest;
        }
        cur = cur * 2;
        if cur == first_one {
            // We have found a loop.
            if start.len() + rest.len() >= 30 {
                return "ERROR".to_string();
            }
            rest.pop();
            return start.to_owned() + "(" + &rest + ")";
        }
        // Process
        if cur >= factor {
            if first_one == 0 {
                first_one = cur;
                start.pop();
                rest += "01";
            } else {
                rest += "1";
            }
            cur -= factor;
        } else if first_one == 0 {
            start += "0";
        } else {
            rest += "0";
        }
    }
    "ERROR".to_string()
}

fn main() {
    let n: f32 = 0.72;
    let expected = "(01011100001010001111)";
    let received = binary_to_string(n);
    assert_eq!(received, expected);
    assert_eq!(binary_to_string(0.5), "01");
    assert_eq!(binary_to_string(0.625), "0101");
    assert_eq!(binary_to_string(0.0625), "00001");
    assert_eq!(binary_to_string(0.00625), "0000000(0110)");
    assert_eq!(binary_to_string(0.000625), "ERROR");
    assert_eq!(
        binary_to_string(0.9879873290843876423894762384762934237023978),
        "ERROR"
    );
}
