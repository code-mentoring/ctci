#ifndef QUEUE_H
#define QUEUE_H

#include <vector>
#include <assert.h>
#include <iostream>

template<class T>
class Queue
{
public:
    Queue();
    void queue(T t);
    T dequeue();
    void print();

private:
    std::vector<T> items_;
};

template <class T>
Queue<T>::Queue()
{

};

template <class T>
void Queue<T>::queue(T t)
{
    items_.push_back(t);
};

template <class T>
void Queue<T>::print()
{
    for (T n : items_)
    {
        std::cout << n << ", ";
    }
    std::cout << std::endl;
};

template <class T>
T Queue<T>::dequeue()
{
    assert(items_.size() > 0);
    T front = items_.front();
    items_.erase(items_.begin());
    return front;
};

#endif // QUEUE_H
