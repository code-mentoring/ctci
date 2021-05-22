#pragma once

#include <vector>
#include <stdlib.h>

class BinaryNode
{
public:
    BinaryNode(int value) : value(value) {}
    BinaryNode(int value, BinaryNode *left, BinaryNode *right) : value(value), left(left), right(right) {}
    int value;
    BinaryNode *left = nullptr;
    BinaryNode *right = nullptr;

    bool isLeaf() { return left == nullptr && right == nullptr; }
};

int height(BinaryNode *node)
{
    if (!node) return 0;

    // height of left
    int leftHeight = 0;
    if (node->left)
    {
        leftHeight = height(node->left); 
    }

    int rightHeight = 0;
    if (node->right)
    {
        rightHeight = height(node->right);
    }

    return std::max(leftHeight, rightHeight) + 1;
}

// 4.4 - check balanced
bool isBalanced(BinaryNode *node)
{
    if (!node) return true;
    return abs(height(node->left) - height(node->right)) <= 1;
}

// 4.5 - validate BST
bool isBinarySearchTree(BinaryNode *root)
{
    if (!root)
    {
        return true;
    }

    std::vector<BinaryNode *> nodes; 
    nodes.push_back(root);

    while (!nodes.empty())
    {
        BinaryNode *node = nodes.front();
        //vprint("Comparing ", node->value);
        if (node->left)
        {
            //vprint("To " , node->left->value);
            if (node->left->value > node->value)
            {
                return false;
            }
            nodes.push_back(node->left);
        }
        if (node->right)
        {
            //vprint("To " , node->right->value);
            if (node->right->value <= node->value)
            {
                return false;
            }
            nodes.push_back(node->right);
        }
        //vprint("Deleting : ", node->value);
        nodes.erase(nodes.begin());
        delete node;
    }

    return true;
}
