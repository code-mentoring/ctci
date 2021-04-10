#include <iostream>

#include "stack.h"
#include "queue.h"
#include "stackmin.h"
#include "setofstacks.h"
#include "myqueue.h"

void testStack();
void testQueue();
void testStackMin();
void testSetOfStacks();
void testMyQueue();

int main()
{
    // testStack();
    // testQueue();
    // testStackMin();

//    std::cout << "Testing Set of stacks: " <<std:: endl;
//    testSetOfStacks();

    testMyQueue();
    std::cout << "Done." <<std:: endl;
    return 0;
}

void testStack()
{
    Stack<int> s;
    s.push(5);
    s.push(6);
    s.push(7);
    s.pop();
    s.print();
}

void testQueue()
{
    Queue<int> q;
    q.queue(5);
    q.queue(6);
    q.queue(7);
    q.queue(8);
    q.dequeue();
    q.print();
}

void testStackMin()
{
    StackMin<int> s;
    s.push(5);
    s.push(4);
    s.push(3);
    std::cout << s.min() << std::endl;
    s.pop();
    std::cout << s.min() << std::endl;
    s.push(5);
    std::cout << s.min() << std::endl;
    s.push(4);
    std::cout << s.min() << std::endl;
    s.pop();
    std::cout << s.min() << std::endl;

    s.push(1);
    s.push(0);
    std::cout << s.min() << std::endl;
    s.pop();
    std::cout << s.min() << std::endl;
}

void testSetOfStacks()
{
    SetOfStacks<int> s;
    s.push(1);
    s.push(2);
    s.push(3);
    s.push(4);
    s.push(5);
    s.push(6);
    s.push(7);
    s.push(8);
    s.push(9);
    s.push(10);
    s.push(11);
    s.print();
    s.pop();
    s.pop();
    s.print();
}

void testMyQueue()
{
    MyQueue<int> q;
    q.queue(1);
    q.queue(2);
    q.queue(3);
    q.print();
    q.dequeue();
    q.print();
    q.dequeue();
    q.print();
    q.dequeue();
    q.print();
    q.queue(5);
    q.print();
}
