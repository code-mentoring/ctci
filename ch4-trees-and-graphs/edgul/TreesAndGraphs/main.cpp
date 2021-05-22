#include <iostream>

#include <vector>
#include <assert.h>
#include <numeric>
#include "Node.h"
#include "Tree.h"
#include "Utils.h"

bool VERBOSE = false;

int main()
{
    // tree
    Node *treeSecond = new Node(2, { new Node(5), new Node(6) });
    Node *treeThird  = new Node(3, { new Node(7) });
    Node *tree = new Node(1, { treeSecond , treeThird, new Node(4)});

    // linked list with cycle
    Node *linkedListTail = new Node(4);
    Node *third = new Node(3,      { linkedListTail });
    Node *second = new Node(2,     { third  });
    Node *linkedList = new Node(1, { second });
    third->nodes.push_back(second); // create cycle

    // tests - route between
    assert(routeBetween(linkedList, linkedList));     // pretty basic
    assert(routeBetween(linkedList, linkedListTail)); // cycle doesn't throw off
    assert(!routeBetween(linkedList, tree));          // different structures
    assert(!routeBetween(treeSecond, treeThird));     // no path from root child to another root child

    // BinarySearchTree prep
    BinaryNode *bstValid = new BinaryNode( 5, new BinaryNode(3), new BinaryNode(6));
    BinaryNode *bstValid1 = new BinaryNode(5, new BinaryNode(3, new BinaryNode(2), new BinaryNode(4)), new BinaryNode(6, new BinaryNode(6), new BinaryNode(7)));
    BinaryNode *bstInvalid1 = new BinaryNode(5, new BinaryNode(6), new BinaryNode(7));
    BinaryNode *bstInvalid2 = new BinaryNode(5, new BinaryNode(4), new BinaryNode(5));

    // tests - bst check
    assert(isBinarySearchTree(bstValid));
    assert(isBinarySearchTree(bstValid1));
    assert(!isBinarySearchTree(bstInvalid1));
    assert(!isBinarySearchTree(bstInvalid2));

    BinaryNode *balancedTree0 = new BinaryNode(1);
    BinaryNode *balancedTree1 = new BinaryNode(1, new BinaryNode(1), nullptr);
    BinaryNode *balancedTree2 = new BinaryNode(1, new BinaryNode(1), new BinaryNode(1));
    BinaryNode *balancedTree3 = new BinaryNode(1, new BinaryNode(1, new BinaryNode(1), nullptr), new BinaryNode(1));
    BinaryNode *balancedTree4 = new BinaryNode(1, new BinaryNode(1), new BinaryNode(1, new BinaryNode(1), nullptr));
    BinaryNode *unbalancedTree0 = new BinaryNode(1, new BinaryNode(2, new BinaryNode(3), nullptr), nullptr); 
    BinaryNode *unbalancedTree1 = new BinaryNode(1, nullptr, new BinaryNode(2, new BinaryNode(3), nullptr)); 
    BinaryNode *unbalancedTree2 = new BinaryNode(1, nullptr, new BinaryNode(2, nullptr, new BinaryNode(3))); 
    assert(isBalanced(balancedTree0));
    assert(isBalanced(balancedTree1));
    assert(isBalanced(balancedTree2));
    assert(isBalanced(balancedTree3));
    assert(isBalanced(balancedTree4));
    assert(!isBalanced(unbalancedTree0));
    assert(!isBalanced(unbalancedTree1));
    assert(!isBalanced(unbalancedTree2));
    
    return 0;
}
