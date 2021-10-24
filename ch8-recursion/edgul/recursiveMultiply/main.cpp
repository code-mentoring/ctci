#include <iostream>
#include <functional>
#include <assert.h>

int recursiveMultiply(int x, int y, int accum = 0) {
    if (y == 0) return accum;
   
    std::function<int(int,int)> accumFunc = std::plus<int>();
    if (y < 0) accumFunc = std::minus<int>();
   
    std::function<int(int,int)> iterFunc = std::minus<int>();
    if (y < 0) iterFunc = std::plus<int>();

    return recursiveMultiply(x, 
                             iterFunc(y,1), 
                             accumFunc(accum,x));
}

// doesn't support negative numbers (yet)
int recursiveMultiply_withBitShift(int x, int y, int accum = 0)
{
    if (y == 0) return accum;
    if (y > 0){
        if (y % 2 == 0)
        {
            accum = accum + (x << 1);
            y -= 2;
        }
        if (y % 2 == 1)
        {
            accum += x;
            y -=1;
        }
    }

    return recursiveMultiply_withBitShift(x, y, accum);
}

using intBiFunc = std::function<int(int,int,int)>;
void testRecursiveMultiply(intBiFunc f) {
    assert(f(0,0,0)==0);
    assert(f(0,5,0)==0);
    assert(f(5,0,0)==0);
    assert(f(1,1,0)==1);
    assert(f(1,2,0)==2);
    assert(f(2,1,0)==2);
    assert(f(1,3,0)==3);
    assert(f(3,1,0)==3);
    assert(f(3,2,0)==6);
    assert(f(2,3,0)==6);
    assert(f(2,5,0)==10);
    assert(f(5,2,0)==10);
    assert(f(5,3,0)==15);
    assert(f(3,5,0)==15);
}

int main(int argc, char **argv) {
    testRecursiveMultiply(recursiveMultiply_withBitShift);
    return 0;
}
