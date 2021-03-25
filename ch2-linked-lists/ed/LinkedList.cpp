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

optional<int> LinkedList::kthLast(int k)
{
    if (!node_) return optional<int>();
    return node_->kthLast(k);
}

LinkedList *LinkedList::partitioned(int value)
{
    if (!node_)
    {
        return new LinkedList();
    }

    Node *leftTail = nullptr;
    Node *leftHead = nullptr;
    Node *rightTail = nullptr;
    Node *rightHead = nullptr;

    // build two lists - O(n)
    Node *iter = node_;
    if (iter->value_ < value) 
    {
        leftHead = new Node(iter->value_);
        leftTail = leftHead;
    }
    else 
    {
        rightHead = new Node(iter->value_);
        rightTail = rightHead;
    }
    while (iter->next_)
    {
        iter = iter->next_;
        if (iter->value_ < value)
        {
            if (!leftHead) 
            {
                leftHead = new Node(iter->value_);
                leftTail = leftHead;
            }
            else
            {
                leftTail->next_ = new Node(iter->value_);
                leftTail = leftTail->next_;
            }
        }
        else
        {
            if (!rightHead) 
            {
                rightHead = new Node(iter->value_);
                rightTail = rightHead;
            }
            else
            {
                rightTail->next_ = new Node(iter->value_);
                rightTail = rightTail->next_;
            }
        }
    }

    //leftHead->print();
    //rightHead->print();

    // concat the lists - O(1)
    LinkedList *result = new LinkedList();
    if (leftHead)
    {
        result->node_ = leftHead;
        if (rightHead)
        {
            leftTail->next_ = rightHead;
        }
    }
    else if (rightHead)
    {
        result->node_ = rightHead;
    }

    return result;
}

Node *LinkedList::concat(Node *left, Node *right)
{
    if (!left)
    {
        return right;
    }

    if (!right)
    {
        return left;
    }
    
    Node *leftTail = tail(left);
    leftTail->next_ = right;
    return left;
}

Node *LinkedList::tail(Node *node)
{
    if (!node)
    {
        return nullptr;
    }

    Node *iter = node;
    while (iter->next_)
    {
        iter = iter->next_;
    }

    return iter;
}

Node* LinkedList::kth(int k)
{
    int count = 0;
    Node *iter = node_;
    while (iter->next_ != nullptr)
    {
        iter = iter->next_;
        count++;
    }

    if (count == k)
    {
        return iter;
    }

    return nullptr; 
}
