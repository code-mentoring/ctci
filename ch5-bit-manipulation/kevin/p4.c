#include <stdio.h>
#include <stdint.h>

void print_binary(uint16_t n) {
    printf("input %d\n", n);
    char buffer[17];
    buffer[16] = '\0';
    size_t i = 0;
    while (n > 0) {
        buffer[15-i] = ((n&1==1) ? '1' : '0');
        ++i;
        n >>= 1;
    }
    //printf("%zu\n", i);
    for (size_t j = i+1; j <= 15; ++j) {
        buffer[15-j] = '0';
    }
    printf("%s", buffer);
}

uint16_t smallest_bit(uint16_t n) {
    return n & (~(n-1));
}

uint16_t next_biggest(uint16_t n) {
    uint16_t s = smallest_bit(n);
    if (s == 0) {
        return 0;
    }
    size_t zeroed_bits = 0;
    for (uint16_t m = s; ((m & n) != 0) && (m>0); m <<= 1) {
        ++zeroed_bits;
    }
    printf("zeroed %zu\n", zeroed_bits);
    return n + s + (1 << (zeroed_bits-1))-1;
}

int main() {
    uint16_t ns[9] = {0, 0xFFFF, 0x8000, 0x0F00, 0x0004, 0xFF01, 7, 9, 13};
    for (size_t i = 0; i < 9; ++i) {
        printf("==============\n");
        print_binary(ns[i]);
        printf(" <-- number\n");
        print_binary(next_biggest(ns[i]));
        printf(" <-- next biggest\n");
    }
}
