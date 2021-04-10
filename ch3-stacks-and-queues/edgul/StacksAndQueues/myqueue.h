#pragma once

#include "stack.h"

template<class T>
class MyQueue
{
public:
    MyQueue() {}
    void queue(T t);
    T dequeue();
    void print();

private:
    Stack<T> mainStack_;
    Stack<T> tempStack_; 
};

template<class T> void MyQueue<T>::queue(T t)
{
    mainStack_.push(t);
};

template<class T> T MyQueue<T>::dequeue()
{
    int size = mainStack_.size();
    for (int i = 0; i < size; i++)
    {
        tempStack_.push(mainStack_.pop());
    }

    T result = tempStack_.pop();
    int tempSize = tempStack_.size();
    for (int i = 0; i < tempSize; i++)
    {
        mainStack_.push(tempStack_.pop());
    }
    return result;
}

template<class T> void MyQueue<T>::print()
{
    mainStack_.print();
}
