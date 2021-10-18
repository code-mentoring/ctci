#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

void print(const std::set<int> &s) {
    std::cout << "{ ";
    for (const auto &val : s)
    {
        std::cout << val << " ";
    }
    std::cout << "}" << std::endl;
}

// returns vector of non-strict subsets
// destroys the input set
// copying could also be improved
std::vector<std::set<int>> power_set(std::set<int> &set) {
    if (set.size() == 0) return {};
    if (set.size() == 1) return { set }; 

    // get all subsets without first item 
    int val = *set.begin();
    set.erase(set.begin());
    std::vector<std::set<int>> inner_subsets = power_set(set); 
   
    // copy all the subsets into result
    std::vector<std::set<int>> result = inner_subsets;

    // add the first item set into result 
    result.push_back({val});
    
    // add the first item to each inner subset
    std::for_each(inner_subsets.begin(), inner_subsets.end(), 
        [&val, &result](auto &subset) {
            std::set<int> s = subset;
            s.insert(val);
            result.push_back(s);
        }
    );
    
    return result;
}

void print(const std::vector<std::set<int>> &vec)
{
    std::cout << "{" << std::endl;
    for (const auto &set : vec)
    {
        std::cout << " ";
        print(set);
    }
    std::cout << "}" << std::endl;
}

int main(int argc, char **argv){
    
    std::set<int> empty_set{};
    std::set<int> single_set{1};
    std::set<int> simple_set_two{1,2};
    std::set<int> simple_set{1,2,3};
    std::set<int> simple_set_four{1,2,3,4};

    std::cout << "Empty set: " << std::endl;
    print(power_set(empty_set));
    std::cout << "Single set: " << std::endl;
    print(power_set(single_set));
    std::cout << "Simple set two: " << std::endl;
    print(power_set(simple_set_two));
    std::cout << "Simple set: " << std::endl;
    print(power_set(simple_set));
    std::cout << "Simple set four: " << std::endl;
    print(power_set(simple_set_four));
    return 0;
}
