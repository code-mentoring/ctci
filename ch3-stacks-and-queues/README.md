Stacks And Queues
-----------------

See text (or web search) for sample stack and queue implementation.

3.2
Stack Min: 
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum eiement? 
Push, pop and min should all operate in 0(1) time.

3.3
Stack of Plates:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
(that is, pop() should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt (int index) which performsa pop operation on a specific sub-stack.

3.4
Queue via Stacks: 
Implement a MyQueue class which implements a queue using two stacks.

