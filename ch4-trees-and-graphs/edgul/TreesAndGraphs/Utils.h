#pragma once

#include <iostream>
#include <vector>
#include <numeric>
#include <assert.h>

extern bool VERBOSE;

std::vector<int> range(int start, int end)
{
    assert(start <= end);
    std::vector<int> l(end-start);
    std::iota(l.begin(), l.end(), start);
    return l;
}

template<class T>
void vprint(std::string text, T t)
{
    if (VERBOSE) std::cout << text.c_str() << t << std::endl;
}

