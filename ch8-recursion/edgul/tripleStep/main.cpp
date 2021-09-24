#include <iostream>
#include <chrono>
#include <functional>
#include <unordered_map>

// basic -- repeats computations, very slow
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

// memoized -- much faster as we don't recompute on the same inputs
int waysToClimbStairsMemoized(int n)
{
    static std::unordered_map<int,int> result;
   
    // only compute if we don't already have an answer on this input
    // store the result for later 
    if (result.find(n) == result.end())
    {
        // same function as above
        auto func = [](int n){
            if      (n <= 0) return 0; 
            else if (n == 1) return 1;
            else if (n == 2) return 2;
            else if (n == 3) return 4;
            return waysToClimbStairsMemoized(n-1) +
                   waysToClimbStairsMemoized(n-2) +
                   waysToClimbStairsMemoized(n-3);
        };
    
        result.insert(std::pair<int,int>(n, func(n)));
    }

    return result.at(n);
}

// helper function to show the timings 
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
    int input = 35;
    timeFunctionCall(waysToClimbStairs, input); 
    timeFunctionCall(waysToClimbStairsMemoized, input);
    timeFunctionCall(waysToClimbStairsMemoized, input);
    return 0;
}


