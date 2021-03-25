#pragma once

#include "Node.h"

class LinkedList
{
public:
    explicit LinkedList();

    bool empty() const;

    void print();
    void append(int value);
    void remove(int value);

    void removeDupsSlow();
    void removeDups();
    optional<int> kthLast(int k);

    Node *kth(int k);

    LinkedList *partitioned(int value);

private:
    Node *node_;

    Node *concat(Node *left, Node *right);
    Node *tail(Node *node);

    bool friend operator==(const LinkedList &lhs, const LinkedList &rhs);
    bool friend operator!=(const LinkedList &lhs, const LinkedList &rhs);
};

inline bool operator==(const LinkedList &lhs, const LinkedList &rhs)
{
    if (!lhs.node_) return !rhs.node_; 
    if (!rhs.node_) return false;       
    return *lhs.node_ == *rhs.node_;
}

inline bool operator !=(const LinkedList &lhs, const LinkedList &rhs)
{
    return !(lhs == rhs);
}
