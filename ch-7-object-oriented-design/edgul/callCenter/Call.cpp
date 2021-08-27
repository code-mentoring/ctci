#include "Call.h"

#include <cstdlib>
#include <ctime>

Call::Call(CallLevel level) :
        level(level) 
{
    srand(time(0));
    duration = rand() % 90 + 10; // 10 -> 100
}
