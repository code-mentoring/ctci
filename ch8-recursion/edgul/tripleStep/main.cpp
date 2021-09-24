#include <iostream>
#include <chrono>
#include <functional>

int waysToClimbStairs(int n)
{
    if      (n <= 0) return 0; 
    else if (n == 1) return 1;
    else if (n == 2) return 2;
    else if (n == 3) return 4;
    
    return waysToClimbStairs(n-1) +
           waysToClimbStairs(n-2) +
           waysToClimbStairs(n-3);
}

void timeFunctionCall(std::function<int(int)> f, int n)
{
    using timept = std::chrono::time_point<std::chrono::system_clock>;

    timept start = std::chrono::system_clock::now();
    int temp = f(n);
    timept end = std::chrono::system_clock::now();

    std::chrono::duration<double> elapsed_seconds = end - start;
    std::cout << "f(" << n  << ") -> " << temp 
              << " in " << elapsed_seconds.count() << std::endl;
}

int main(int argc, char **argv)
{
    timeFunctionCall(waysToClimbStairs, 30); 
    return 0;
}


