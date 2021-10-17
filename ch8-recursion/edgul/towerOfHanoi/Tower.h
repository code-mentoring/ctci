#pragma once

#include <numeric>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>
#include <memory>
#include "Stack.h"
#include "Ring.h"

using stack_ptr = std::shared_ptr<Stack<Ring>>;
class Tower {
public:
    enum class Pole { LEFT, MID, RIGHT };
    Tower(int size) {
        std::vector<int> temp(size);
        std::iota(temp.begin(), temp.end(), 0);
        std::reverse(temp.begin(), temp.end());

        stack_ptr left = stack_ptr(new Stack<Ring>());
        for (int i : temp)
        {
            left->push(Ring(i));
        }
        rings.insert(std::pair(Pole::LEFT, left));
        rings.insert(std::pair(Pole::MID, new Stack<Ring>()));
        rings.insert(std::pair(Pole::RIGHT, new Stack<Ring>()));
    }
    bool move(Pole src, Pole dest) {
        assert(src != dest);
        auto ringSource = rings[src]->peek();
        assert(ringSource.has_value());
        auto ringDest = rings[dest]->peek();
        if (ringDest.has_value())
        {
            if (ringSource.value() > ringDest.value()){
                //std::cout << "Cannot move " << ringSource.value() << " on top of " << ringDest.value() << std::endl;
                return false;
            }
        }
        rings[dest]->push(rings[src]->pop().value());
        return true;
    }
    void print()
    {
        std::cout << "L: ";
        rings[Pole::LEFT]->print();
        std::cout << "M: ";
        rings[Pole::MID]->print();
        std::cout << "R: ";
        rings[Pole::RIGHT]->print();
        std::cout << std::endl;
    }

    std::unordered_map<Pole, stack_ptr> rings;
};
