#ifndef STACK_H
#define STACK_H

#include <vector>
#include <assert.h>
#include <iostream>

template<class T>
class Stack
{
public:
    Stack() {};
    void push(T t);
    T pop();
    T peek();
    int size();
    bool empty();
    void print();
private:
    std::vector<T> items_;
};

template <class T> void Stack<T>::push(T t)
{
    items_.push_back(t);
};

template <class T> void Stack<T>::print()
{
    for (T n : items_)
    {
        std::cout << n << ", ";
    }
    std::cout << std::endl;
};

template <class T> int Stack<T>::size()
{
    return items_.size();
}

template <class T> bool Stack<T>::empty()
{
    return items_.size() == 0;
}

template <class T> T Stack<T>::pop()
{
    assert(!empty());
    T back = items_.back();
    items_.pop_back();
    return back;
};

template <class T> T Stack<T>::peek()
{
    assert(!empty());
    return items_.back();
};



#endif // STACK_H
