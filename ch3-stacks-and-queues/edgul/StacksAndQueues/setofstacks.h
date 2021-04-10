#ifndef SETOFSTACKS_H
#define SETOFSTACKS_H

#include "stack.h"

template <class T>
class SetOfStacks
{
public:
    SetOfStacks() {}
    void push(T t);
    T pop();
    T peek();
    bool empty();
    void print();

private:
    std::vector<Stack<T>> stacks_;
    int capacity_ = 5;
};

template <class T> void SetOfStacks<T>::push(T t)
{
    if (stacks_.size() == 0 || stacks_.at(stacks_.size()-1).size() >= capacity_)
    {
        stacks_.push_back(Stack<T>());
    }
    stacks_.at(stacks_.size()-1).push(t);
};

template <class T> void SetOfStacks<T>::print()
{
    for (Stack<T> stack : stacks_)
    {
        stack.print();
    }
    std::cout << std::endl;
};

template <class T> bool SetOfStacks<T>::empty()
{
    return stacks_.size() == 0;
}

template <class T> T SetOfStacks<T>::pop()
{
    assert(!empty());
    T back = stacks_.at(stacks_.size()-1).pop();
    if (stacks_.at(stacks_.size()-1).empty())
    {
        stacks_.pop_back();
    }
    return back;
};

template <class T> T SetOfStacks<T>::peek()
{
    assert(!empty());
    return stacks_.at(stacks_.size()-1).peek();
};

#endif // SETOFSTACKS_H
