#include "CircularArray.h"
#include <iostream>

void print(CircularArray<int> &arr)
{
    std::for_each(arr.begin(), arr.end(), 
            [](auto i) { std::cout << i << " "; });
    std::cout << std::endl;
}

int main(int argc, char *argv[])
{

    CircularArray<int> arr(5);
    arr[0] = 5;
    arr[1] = 6;
    arr[2] = 7;
    arr[3] = 8;
    arr[4] = 9;
    print(arr);

    arr.rotate(1);
    print(arr);

    return 0;
}
