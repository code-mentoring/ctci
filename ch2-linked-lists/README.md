Ch2 - Linked Lists
------------------

Here is a some potential pseudo-code for linked list implementation:

class Node 
{
    Node next = null;
    int data;

    public Node(int d) {
        data = d;
    }
    
    void appendToTail(int d) {
        Node end = new Node(d);
        Node n = this;
        while (n.next 1= null) {
            n = n.next;
        }
        n.next = end;
    }
}

Questions:

2.1
Remove Dups: Write code to remove duplicates from an unsorted linked list.
FOLLOW UP
How would you solve this problem if a temporary buffer is not allowed?

2.2
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

2.3
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
Input: the node c from the linked list a -> b -> c -> d -> e -> f
Result: nothing is returned, but the new linked list looks like a -> b -> d -> e -> f

--- Session 2

2.4 
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

2.7
Intersection; Given two (singly) linked lists, determine if the two lists intersect. Return the inter-
secting node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the j t h node of the second
linked list, then they are intersecting.

2.8
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A - > 8 - > C - > D - > E - > C [the same C as earlier]
Output: C

