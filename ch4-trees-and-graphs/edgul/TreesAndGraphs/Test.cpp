#include "Test.h"

#include <vector>
#include <assert.h>
#include <numeric>
#include "Node.h"
#include "BinaryNode.h"

namespace Test
{

void testSubTree()
{
    std::cout << "Testing sub tree function...\n";
    BinaryNode *treeJustOne =             new BinaryNode(1);
    BinaryNode *treeOneWithLeftOne =      new BinaryNode(1, new BinaryNode(1), nullptr);
    BinaryNode *treeOneWithRightOne =      new BinaryNode(1, nullptr, new BinaryNode(1));
    BinaryNode *treeOneWithChildrenOnes = new BinaryNode(1, new BinaryNode(1), new BinaryNode(1));

    BinaryNode *treeJustTwo = new BinaryNode(2);
    BinaryNode *treeTwoWithLeftOne =      new BinaryNode(2, new BinaryNode(1), nullptr);
    BinaryNode *treeTwoWithRightOne =     new BinaryNode(2, nullptr,           new BinaryNode(1));
    BinaryNode *treeTwoWithChildrenOnes = new BinaryNode(2, new BinaryNode(1), new BinaryNode(1));

    assert(isSubTree(treeJustOne, treeJustOne));
    assert(isSubTree(treeJustOne, treeOneWithLeftOne));
    assert(!isSubTree(treeOneWithLeftOne, treeJustOne));

    assert(!isSubTree(treeOneWithLeftOne, treeOneWithChildrenOnes));
    assert(!isSubTree(treeOneWithRightOne, treeOneWithChildrenOnes));

    assert(isSubTree(treeJustOne, treeTwoWithLeftOne));
    assert(!isSubTree(treeJustTwo, treeTwoWithLeftOne));

    assert(isSubTree(treeJustOne, treeTwoWithRightOne));
    assert(!isSubTree(treeJustTwo, treeTwoWithRightOne));

    assert(!isSubTree(treeTwoWithLeftOne, treeTwoWithChildrenOnes));
    assert(!isSubTree(treeTwoWithRightOne, treeTwoWithChildrenOnes));


    BinaryNode *treeOneTwoThree = new BinaryNode(1, new BinaryNode(2), new BinaryNode(3));
    BinaryNode *treeFourLeftOneTwoThree = new BinaryNode(4, new BinaryNode(1, new BinaryNode(2), new BinaryNode(3)), nullptr);
    BinaryNode *treeFourRightOneTwoThree = new BinaryNode(4, nullptr, new BinaryNode(1, new BinaryNode(2), new BinaryNode(3)));

    assert(isSubTree(treeOneTwoThree, treeFourLeftOneTwoThree));
    assert(isSubTree(treeOneTwoThree, treeFourRightOneTwoThree));
}

void testNodesAndTrees()
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


    std::vector<ProjDep> validBuildOrder0;
    validBuildOrder0.push_back(ProjDep(1,0));
    std::vector<int> one = {1};
    assert(build_order(validBuildOrder0) == one);

    std::vector<ProjDep> validBuildOrder1;
    std::vector<int> twoOne = {2,1};
    validBuildOrder1.push_back(ProjDep(1,2));
    assert(build_order(validBuildOrder1) == twoOne);

    std::vector<ProjDep> validBuildOrder2;
    validBuildOrder2.push_back(ProjDep(1,2));
    validBuildOrder2.push_back(ProjDep(2,3));
    std::vector<int> threeTwoOne = {3,2,1};
    assert(build_order(validBuildOrder2) == threeTwoOne);

    std::vector<ProjDep> validBuildOrder3;
    validBuildOrder3.push_back(ProjDep(1,2));
    validBuildOrder3.push_back(ProjDep(3,2));
    std::vector<int> twoOneThree = {2, 1, 3};
    std::vector<int> twoThreeOne = {2, 3, 1};
    assert(build_order(validBuildOrder3) == twoOneThree ||
           build_order(validBuildOrder3) == twoThreeOne);

    std::vector<ProjDep> validBuildOrder4;
    validBuildOrder4.push_back(ProjDep(1,2));
    validBuildOrder4.push_back(ProjDep(1,3));
    validBuildOrder4.push_back(ProjDep(2,4));
    validBuildOrder4.push_back(ProjDep(3,4));
    std::vector<int> fourTwoThreeOne = {4,2,3,1};
    std::vector<int> fourThreeTwoOne = {4,3,2,1};
    assert(build_order(validBuildOrder4) == fourTwoThreeOne||
           build_order(validBuildOrder4) == fourThreeTwoOne);

    std::vector<ProjDep> invalidBuildOrder0;
    invalidBuildOrder0.push_back(ProjDep(1,2));
    invalidBuildOrder0.push_back(ProjDep(2,1));
    std::vector<int> empty;
    assert(build_order(invalidBuildOrder0) == empty);

    std::vector<ProjDep> invalidBuildOrder1;
    invalidBuildOrder1.push_back(ProjDep(1,2));
    invalidBuildOrder1.push_back(ProjDep(2,3));
    invalidBuildOrder1.push_back(ProjDep(3,1));
    assert(build_order(invalidBuildOrder1) == empty);

}

} // namespace
