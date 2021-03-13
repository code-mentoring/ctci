#include "LinkedList.h"
#include <iostream>

LinkedList::LinkedList() : node_(nullptr)
{

}

bool LinkedList::empty() const
{
    return !node_;
}

void LinkedList::append(int value)
{
    if (!node_)
    {
        node_ = new Node(value);
        return;
    }

    node_->append(value);
}

void LinkedList::remove(int value)
{
    if (!node_) return;
    
    if (node_->value() == value)
    {
        Node *tmp = node_;
        node_ = node_->next_;
        delete tmp; 
        return;
    }
    node_->remove(value);
}

void LinkedList::print()
{
    if (!node_) 
    {
        std::cout << std::endl;
        return;
    }
    node_->print();
}
    
void LinkedList::removeDupsSlow()
{
    if (!node_)
    {
        return;
    }
    node_->removeDupsSlow();
}
    
void LinkedList::removeDups()
{
    if (!node_)
    {
        return;
    }

    std::set<int> unique;
    unique.insert(node_->value());
    node_->removeDups(unique);
}

optional LinkedList::kthLast(int k)
{
    if (!node_) return optional();
    return node_->kthLast(k);
}
