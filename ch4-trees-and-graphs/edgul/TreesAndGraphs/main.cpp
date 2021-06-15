#include <iostream>

#include "Test.h"

bool VERBOSE = false;

// 4.1  - route between two nodes - Node.h -> bool routeBetween(Node *start, Node *end);
// 4.4  - check balanced          - Tree.h -> bool isBalanced(BinaryNode *node)\
// 4.5  - validate BST            - Tree.h -> bool isBinarySearchTree(BinaryNode *root)
// 4.6  - build order             - Node.h -> std::vector<int> build_order(std::vector<ProjDep> projDeps)
// 4.10 - isSubtree               - Tree.h ->

int main()
{
    // Test::testNodesAndTrees();
    Test::testSubTree();

    return 0;
}
