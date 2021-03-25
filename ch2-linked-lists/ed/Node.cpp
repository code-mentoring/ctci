#include "Node.h"
#include <iostream>

Node::Node(int value) : value_(value), next_(nullptr)
{

}

int Node::value() const
{
    return value_;
}

Node & Node::next() const
{
    return *next_;
}

bool Node::nextValid() const
{
    return next_;
}

void Node::print() const
{
    std::cout << value() << " ";
    if (next_) next_->print();
    else std::cout << std::endl;
}

void Node::append(int value)
{
    Node *i = this;
    while (i->next_)
    {
       i = i->next_;
    }

    i->next_ = new Node(value);
}

void Node::remove(int value)
{
    Node *i = this;
    while (i->next_ && i->next_->value() != value)
    {
        i = i->next_;
    }
    
    if (i->next_)
    {
        Node *tmp = i->next_;
        i->next_ = i->next_->next_;
        delete tmp;
    }
}

// 1.1 (a)
// Time complexity: Worst: O(n^2)
// Space complexity: O(1)
void Node::removeDupsSlow()
{
    Node *i = this;
    while (i->next_)
    {
        if (i->next_->value() == value_)
        {
            Node *tmp = i->next_;
            i->next_ = i->next_->next_;
            delete tmp;
            continue;
        }
        i = i->next_;
    }

    if (this->next_)
    {
        this->next_->removeDupsSlow();
    }
}

// 1.1 (b)
// TimeComplexity: Worst: O(n log n) because find and insert takes O(log n)
//                 std::unordered_map instead of set would be:  Average: O(n), Worst: (n^2)
// Space Complexity: Worst O(n) 
void Node::removeDups(std::set<int> uniqueSet)
{
    Node *i = this;
    while (i->next_)
    {
        if (uniqueSet.find(i->next_->value_) != uniqueSet.end()) 
        {
            Node *tmp = i->next_;
            i->next_ = i->next_->next_;
            delete tmp;
        }
        else
        {
            uniqueSet.insert(i->next_->value_);
            i = i->next_;
        }
    }
}

// 1.2 - where k=1 -> last item
// Time complexity O(n) every time
optional<int> Node::kthLast(int k)
{
    Node *first = this;
    Node *second = this;

    // put first k items ahead
    if (k < 1) return optional<int>();
    for (int i = 1; i < k; i++)
    {
        if (!first->next_)
        {
            return optional<int>();
        }
        first = first->next_;
    }

    while (first->next_)
    {
        first = first->next_;
        second = second->next_;
    }
    return optional<int>(second->value());
}
