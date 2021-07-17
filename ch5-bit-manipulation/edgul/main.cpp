
#include <iostream>
#include <bitset>

struct MinAndMax
{
    int min;
    int max;
};

// 4.4
MinAndMax nextSmallestAndLargest(unsigned short x)
{
    MinAndMax result; 
    // todo
    return result;
}

// 4.5 
bool unknownFunction(int n)
{
    return (n & n-1) == 0;
}

void testUnknownFunction()
{
    for (int i = 0; i < 20; i++)
    {
        std::cout << i << " -> " << unknownFunction(i) << std::endl;
    }
}

// 4.6
int numBitsToFlip(unsigned short x, unsigned short y)
{
    int count = 0;
    for (int i = 0; i < 16; i++)
    {
        if ((x >> i & 0x1) != (y >> i & 0x1)) count++;
    }
    return count;
}

void testNumBitsToFlip()
{
    unsigned short x = 8;
    unsigned short y = 15;

    std::cout << "x: " << std::bitset<16>(x) 
              << " y: " << std::bitset<16>(y)
              << " " << numBitsToFlip(x, y) << std::endl; 
}

int main(int argc, char * argv[])
{
    // testUnknownFunction();
    return 0;
}
