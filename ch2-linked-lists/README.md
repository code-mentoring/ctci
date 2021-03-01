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
