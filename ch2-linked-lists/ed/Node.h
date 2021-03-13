#pragma once

#include <iostream>
#include <set>

struct optional
{
    int value;
    bool valid;
    optional(int value) : value(value), valid(true) {}
    optional() : value(0), valid(false) {}
};

class Node
{
public:
    explicit Node(int value); 
    Node(const Node &node) = delete;

    int value() const;
    Node &next() const;
    bool nextValid() const;

    // list-ish
    void print() const;
    void append(int value);
    void remove(int value);

    void removeDupsSlow();
    void removeDups(std::set<int> uniqueSet);

    optional kthLast(int k);

private:
    Node *next_;
    int value_;
   
    friend class LinkedList;
    bool friend operator==(const Node &lhs, const Node &rhs);
    bool friend operator!=(const Node &lhs, const Node &rhs);
};

inline bool operator==(const Node &lhs, const Node &rhs)
{
    if (lhs.value_ == rhs.value_)
    {
        if (!lhs.next_) return !rhs.next_;
        if (!rhs.next_) return false;
        return lhs.next() == rhs.next();
    }
    return false;
}

inline bool operator!=(const Node &lhs, const Node &rhs)
{
    return !(lhs == rhs);
}

    
