#pragma once

#include <iostream>
#include <vector>
#include <assert.h>
#include <numeric>
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

class BinaryNode
{
public:
    BinaryNode(int value) : value(value) {}
    BinaryNode(int value, BinaryNode *left, BinaryNode *right) : value(value), left(left), right(right) {}
    int value;
    BinaryNode *left = nullptr;
    BinaryNode *right = nullptr;
};

