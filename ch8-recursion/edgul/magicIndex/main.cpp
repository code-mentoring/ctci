#include <assert.h>
#include <vector>

// doesn't matter if numbers are unique or not
bool magicIndex(const std::vector<int> &vec, int start_index = 0) {
    if (start_index >= vec.size())       return false;
    if (vec[start_index] == start_index) return true;
    return magicIndex(vec, start_index + 1); 
}

int main(int argc, char **argv) {
    std::vector y1 = {0,1,2,3};
    std::vector y2 = {1,0,0,3};
    std::vector y3 = {0};
    assert(magicIndex(y1));
    assert(magicIndex(y2));
    assert(magicIndex(y3));
   
    std::vector<int> n1 = {};
    std::vector n2 = {1};
    std::vector n3 = {2};
    std::vector n4 = {1,2,3};
    std::vector n5 = {-1,-1,1};
    assert(!magicIndex(n1));
    assert(!magicIndex(n2));
    assert(!magicIndex(n3));
    assert(!magicIndex(n4));
    assert(!magicIndex(n5));
    return 0;
}
