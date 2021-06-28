import sys

def main():
    # Let's say 8 bits for the exponent, 24 bits
    # for the significand. So 0<=e<2^8, 0<=s<2^24,
    # and f = s * 2^-e.
    exp_bits = 8
    significand_bits = 24
    f = 0.625
    if f > 1 or f < 0:
        print("ERROR: number outside range")
        return
    e = 0
    s = 0
    s_bits = 0
    while f > 0 and e < 2**exp_bits and not (s_bits > significand_bits):
        s = (s << 1)
        e += 1
        power_of_2 = 2**-e
        if power_of_2 <= f:
            f -= power_of_2
            s |= 1
        if s > 0:
            s_bits += 1
    if e >= 2**exp_bits:
        print("ERROR: exponent too big")
    elif s_bits > significand_bits:
        print("ERROR: significand can't be represented")
    else:
        print("Exponent:", bin(e), "/", e)
        print("Significand:", bin(s), "/", s)
            
if __name__ == "__main__":
    main()
