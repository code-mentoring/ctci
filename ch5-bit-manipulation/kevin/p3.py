def longest_sequence(n):
    sequences = []
    i = 0
    in_sequence = False
    start = 0
    end = 0
    while n > 0:
        if n&1 == 1:
            if not in_sequence:
                in_sequence = True
                start = i
            end = i
        if in_sequence and (n==1 or (n&1)==0):
            sequences.append((start, end))
            in_sequence = False
        n >>= 1
        i += 1
    longest_seq_length = (0 if not sequences
                            else max(map(lambda seq: seq[1]-seq[0]+1, sequences)))
    # In the worst case, we won't be able to join up any of the
    # sequences, we'll just be able to extend the longest sequence
    # by 1. So compute that first.
    length = 1 + longest_seq_length
    # Try all pairs of sequences, see if they can be connected by
    # a single bit flip.
    for (s1, e1), (s2, e2) in zip(sequences, sequences[1:]):
        if s2 == e1+2:
            length = max(length, e2-s1+1)
    return length

def main():
    print("should be 8:", longest_sequence(0b11011101111))
    print("should be 8:", longest_sequence(0b111111100101))
    print("should be 8:", longest_sequence(0b111101110001110))
    print("should be 1:", longest_sequence(0b0))
    print("should be 2:", longest_sequence(0b1))

if __name__ == "__main__":
    main()
