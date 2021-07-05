import math

def insert_num(N, M, i, j):
    bits_to_represent_M = math.ceil(math.log2(M))
    all_1s_mask = 2**(bits_to_represent_M)-1
    # AND the mask with N to find bits that need
    # to be zero'd, so that there's space for M.
    # XOR this with N again to zero those bits.
    # Then OR N with M so that the zero'd bits
    # take on the value of M.
    return N ^ (N & (all_1s_mask << i)) | (M << i)

def main():
    result = insert_num(0b10000000000, 0b10011, 2, 6)
    print(bin(result))
    print(result == 0b10001001100)

if __name__ == "__main__":
    main()
