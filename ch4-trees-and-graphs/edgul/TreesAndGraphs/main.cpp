#include <iostream>

#include <vector>
#include <assert.h>
#include <numeric>
#include <unordered_set>

const bool VERBOSE = true;

using namespace std;

std::vector<int> range(int start, int end)
{
    assert(start <= end);
    std::vector<int> l(end-start);
    std::iota(l.begin(), l.end(), start);
    return l;
}

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
            cout << "CYCLE DETECTED (Not drawn)" << endl;
            return;
        }

        for (int i : range(0,depth)) { cout << "->"; }
        cout << value << endl;
        visited_ = true;
        for (Node *node : nodes)
        {
            node->print(depth+1);
        }
    }
private:
    bool visited_ = false;
};

void vprint(std::string text, Node *node)
{
    if (VERBOSE) cout << text.c_str() << node << endl;
}

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

    return 0;
}
