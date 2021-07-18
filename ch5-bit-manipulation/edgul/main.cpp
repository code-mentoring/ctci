
#include <iostream>
#include <bitset>
#include <climits>

struct MinAndMax
{
    int min = 0;
    int max = 0;
    bool valid() { return min && max; }
};

int countBits(unsigned short x)
{
    int count = 0;
    for (int i = 0; i < 16; i++)
    {
        if (x >> i & 0x1) count++;
    }
    return count;
}

// 5.4
MinAndMax nextSmallestAndLargest(unsigned short x)
{
    MinAndMax result; 
    int originalCount = countBits(x);

    unsigned short iterDown = x;
    while (iterDown > 0)
    {
        iterDown--;     
        if (countBits(iterDown) == originalCount)
        {
            result.min = iterDown;
            break;
        }
    }

    unsigned short iterUp = x;
    while (iterUp < USHRT_MAX)
    {
        iterUp++;
        if (countBits(iterUp) == originalCount)
        {
            result.max = iterUp;
            break;
        }
    }
    return result;
}

void print(int x)
{
    std::cout << x << " -> " 
        << nextSmallestAndLargest(x).min << " " 
        << nextSmallestAndLargest(x).max << std::endl;
}

void testNextSmallestAndLargest()
{
    for (int i = 0; i < 20; i++)
    {
        print(i);
    }
}

// 5.5 
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

// 5.6
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
    testNextSmallestAndLargest();
    // testUnknownFunction();
    // testNumBitsToFlip();
    return 0;
}
