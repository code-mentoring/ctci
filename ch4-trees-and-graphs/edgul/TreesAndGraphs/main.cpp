#include <iostream>

#include <vector>
#include <assert.h>
#include <numeric>
#include <unordered_set>
#include "Node.h"
#include "Utils.h"

bool VERBOSE = true;

using namespace std;


// 4.1
bool routeBetween(Node *start, Node *end)
{
    vprint("Looking for: ", end );
    vprint("Checking: "   , start);
    if (start == end) return true;

    std::vector<Node *> explore = start->nodes;
    std::unordered_set<Node *> explored; // constant insert and lookup (average), linear insert/lookup for worstcase
    while (explore.size())
    {
        Node *node = explore.at(0);
        explore.erase(explore.begin());

        if (explored.find(node) == explored.end()) // don't double check a cycle or it's children
        {
            vprint("Checking: ", node);
            if (node == end) return true;
            explore.insert(explore.end(), node->nodes.begin(), node->nodes.end());
        }
        explored.insert(node);
    }
    return false;
}

// 4.1 - helper
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

bool isMinimalBinarySearchTree(Node *root) 
{
    return false;
}

int main()
{
    // tree
    Node *treeSecond = new Node(2, { new Node(5), new Node(6) });
    Node *treeThird  = new Node(3, { new Node(7) });
    Node *tree = new Node(1, { treeSecond , treeThird, new Node(4)});
    // tree->print();
    // cout << endl;

    // linked list with cycle
    Node *linkedListTail = new Node(4);
    Node *third = new Node(3,      { linkedListTail });
    Node *second = new Node(2,     { third  });
    Node *linkedList = new Node(1, { second });
    third->nodes.push_back(second); // create cycle
    // linkedList->print();
    // cout << endl;

    // tests
    assert(routeBetween(linkedList, linkedList));     // pretty basic
    assert(routeBetween(linkedList, linkedListTail)); // cycle doesn't throw off
    assert(!routeBetween(linkedList, tree));          // different structures
    assert(!routeBetween(treeSecond, treeThird));     // no path from root child to another root child

    // BinarySearchTree
    BinaryNode *bstValid = new BinaryNode( 5, new BinaryNode(3), new BinaryNode(6));
    BinaryNode *bstValid1 = new BinaryNode(5, new BinaryNode(3, new BinaryNode(2), new BinaryNode(4)), new BinaryNode(6, new BinaryNode(6), new BinaryNode(7)));
    BinaryNode *bstInvalid1 = new BinaryNode(5, new BinaryNode(6), new BinaryNode(7));
    BinaryNode *bstInvalid2 = new BinaryNode(5, new BinaryNode(4), new BinaryNode(5));

    assert(isBinarySearchTree(bstValid));
    assert(isBinarySearchTree(bstValid1));
//    isBinarySearchTree(bstValid1);
    assert(!isBinarySearchTree(bstInvalid1));
    assert(!isBinarySearchTree(bstInvalid2));

    return 0;
}
