# Write a recursive function to multiply two positive integers without using the * operator.
# You can use addition, subtraction, and bit shifting, but you should minimize the number of those operations
# itertools.repeat(val, num), faster than range(), only works with positive integers
import itertools

def main():
    int_a = 2
    int_b = 3

    def recursive_method(num_a, num_b):
        a_times_b = 0

        def add_a_b_times(a, b):
            nonlocal a_times_b
            if b == 0:
                return
            else:
                a_times_b += a
                b -= 1
                add_a_b_times(a, b)

        add_a_b_times(num_a, num_b)
        return a_times_b

    def more_efficient_method(num_a, num_b):
        total = 0
        for _ in itertools.repeat(None, num_b):
            total += num_a
        return total

    print("Using recursion: ", recursive_method(int_a, int_b))
    print("Using itertools: ", more_efficient_method(int_a, int_b))

if __name__ == "__main__":
    main()
