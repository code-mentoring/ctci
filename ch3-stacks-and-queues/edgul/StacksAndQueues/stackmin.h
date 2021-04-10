#ifndef STACKMIN_H
#define STACKMIN_H

#include "stack.h"

template<class T>
class StackMin
{
public:
    StackMin() {};
    void push(T t);
    T pop();
    T peek();
    bool empty();
    T min();
    void print();
private:
    Stack<T> orderStack_;
    Stack<T> minStack_;
};

template <class T> void StackMin<T>::push(T t)
{
    orderStack_.push(t);
    if (minStack_.empty() || minStack_.peek() >= t)
    {
        minStack_.push(t);
    }
};

template <class T> void StackMin<T>::print()
{
    orderStack_.print();
};

template <class T> bool StackMin<T>::empty()
{
    return orderStack_.empty();
}

template <class T> T StackMin<T>::pop()
{
    assert(!empty());
    T back = orderStack_.pop();
    orderStack_.pop();
    if (back == minStack_.peek())
    {
        minStack_.pop();
    }
    return back;
};

template <class T> T StackMin<T>::peek()
{
    return orderStack_.peek();
};

template <class T> T StackMin<T>::min()
{
    assert(!empty());
    return minStack_.peek();
}


#endif // STACKMIN_H
