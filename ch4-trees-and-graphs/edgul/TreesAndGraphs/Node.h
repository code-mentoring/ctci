#pragma once

#include <iostream>
#include <vector>
#include <assert.h>
#include <numeric>
#include <unordered_set>
#include "Utils.h"

class Node
{
public:
    Node(int value) : value(value) {}
    Node(int value, std::vector<Node *> nodes) : value(value), nodes(nodes) {}
    int value;
    std::vector<Node *> nodes;

    void print(int depth = 0)
    {
        if (visited_)
        {
            std::cout << "CYCLE DETECTED (Not drawn)" << std::endl;
            return;
        }

        for (int i : range(0,depth)) { std::cout << "->"; }
        std::cout << value << std::endl;
        visited_ = true;
        for (Node *node : nodes)
        {
            node->print(depth+1);
        }
    }
private:
    bool visited_ = false;
};


// 4.1
bool routeBetween(Node *start, Node *end)
{
    //vprint("Looking for: ", end );
    //vprint("Checking: "   , start);
    if (start == end) return true;

    std::vector<Node *> explore = start->nodes;
    std::unordered_set<Node *> explored; // constant insert and lookup (average), linear insert/lookup for worstcase
    while (explore.size())
    {
        Node *node = explore.at(0);
        explore.erase(explore.begin());

        if (explored.find(node) == explored.end()) // don't double check a cycle or it's children
        {
            //vprint("Checking: ", node);
            if (node == end) return true;
            explore.insert(explore.end(), node->nodes.begin(), node->nodes.end());
        }
        explored.insert(node);
    }
    return false;
}
