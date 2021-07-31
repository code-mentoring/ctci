
#include <iostream>
#include <bitset>
#include <climits>
#include <assert.h>
#include <cstddef>
#include <vector>


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

unsigned short evenMask()
{
    return 0xAAAA;
}

unsigned short oddMask()
{
    return 0x5555;
}

// 5.7
unsigned short pairwiseSwap(unsigned short x)
{
    unsigned short left =  (x << 1) & evenMask();
    unsigned short right = (x >> 1) & oddMask();
    return left | right;
}

void testPairwiseSwap()
{
    assert(pairwiseSwap(1) == 2);
    assert(pairwiseSwap(2) == 1);
    assert(pairwiseSwap(8) == 4);
    assert(pairwiseSwap(4) == 8);
    assert(pairwiseSwap(0x8000) == 0x4000);
    assert(pairwiseSwap(0xC000) == 0xC000);
    assert(pairwiseSwap(0xF000) == 0xF000);
    assert(pairwiseSwap(0xA000) == 0x5000);
    assert(pairwiseSwap(0x00A0) == 0x0050);
}

class Screen
{
public:
    Screen(int width, int height) : width_(width)
    { 
        assert(width_ % 8 == 0);
        bits = std::vector<bool>(width_*height);
    }

    int width() { return width_; }
    int height() { return bits.size()/(width_); }
    void print() 
    {
        int soFar = 0;
        for (bool i : bits)
        {
            std::cout << i;
            soFar++;
            if (soFar % width_ == 0)
            {
                std::cout << "\n";
            }
        }
    }

    // 5.8 -- draws a horizontal line on the screen
    void drawLine(unsigned int x1, unsigned int x2, unsigned int y)
    {
        assert(x1 >= 0 && x1 < width_);
        assert(x2 >= 0 && x2 < width_);
        assert(y  >= 0 && y  < height());

        unsigned char minX = std::min(x1, x2);     
        unsigned char maxX = std::max(x1, x2);
       
        unsigned int start = y * width_ + minX;
        unsigned int end = start + (maxX - minX);

        for (int i = start; i <= end; i++)
        {
            bits[i] = 1;
        }
    }

private:
    std::vector<bool> bits;
    int width_;
}; 

void testDrawLine()
{

    Screen s(24,24);
    s.drawLine(0, 0, 0); // top-left corner
    s.drawLine(23,23,23); // bottom-right corner

    // draw a box
    s.drawLine(10, 20, 7);
    s.drawLine(10, 20, 9);
    s.drawLine(10, 10, 8);
    s.drawLine(20, 20, 8);

    s.print();
}

int main(int argc, char * argv[])
{
    // testNextSmallestAndLargest();
    // testUnknownFunction();
    // testNumBitsToFlip();
    // testPairwiseSwap(); // 5.7
    testDrawLine();
    return 0;
}
