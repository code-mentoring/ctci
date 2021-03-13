#include <iostream>
#include <assert.h>
#include "LinkedList.h"

void testBasicLinkedList();
void testRemoveLinkedList();
void testRemoveDups();
void testRemoveDupsSlow();
void testKthLast();

int main(int argc, char *argv[])
{
    testBasicLinkedList();
    testRemoveLinkedList();
    testRemoveDupsSlow();
    testRemoveDups();
    testKthLast();
    return 0;
}

void testKthLast()
{
    LinkedList l = LinkedList();
    l.append(1);
    l.append(2);
    l.append(3);
    l.append(4);
    l.append(5);

    assert(l.kthLast(0).valid == false);
    assert(l.kthLast(1).valid);
    assert(l.kthLast(5).valid);
    assert(l.kthLast(6).valid == false);
    assert(l.kthLast(1).value == 5); // last value
    assert(l.kthLast(2).value == 4);
    assert(l.kthLast(3).value == 3);
    assert(l.kthLast(4).value == 2);
    assert(l.kthLast(5).value == 1);

}

void testBasicLinkedList()
{
    LinkedList l_empty = LinkedList();

    LinkedList l_three = LinkedList();
    l_three.append(3);
   
    LinkedList l_five = LinkedList();
    l_five.append(5);
    LinkedList l_5 = LinkedList();
    l_5.append(5);

    LinkedList l_15 = LinkedList();
    l_15.append(1);
    l_15.append(2);
    l_15.append(3);
    l_15.append(4);
    l_15.append(5);

    assert(l_empty != l_five);
    assert(!(l_empty == l_five));
    assert(l_5 == l_five);
    assert(!(l_5 != l_five));
    assert(l_three != l_five);
    assert(!(l_three == l_five));
    assert(l_three != l_15);
    assert(!(l_three == l_15));
}

void testRemoveLinkedList()
{
    LinkedList l = LinkedList();
    l.append(1);
    l.append(2);
    l.append(3);
    l.append(4);
    l.remove(3);

    LinkedList l124 = LinkedList();
    l124.append(1);
    l124.append(2);
    l124.append(4);
    assert(l124 == l); 

    l.remove(4);

    LinkedList l12 = LinkedList();
    l12.append(1);
    l12.append(2);
    assert(l == l12);

    l.remove(1);

    LinkedList l2 = LinkedList();
    l2.append(2);
    assert(l == l2);

    l.remove(2);

    LinkedList l0 = LinkedList();
    assert(l == l0);

}

void testRemoveDups()
{
    LinkedList l = LinkedList();
    l.append(1);
    l.append(1);
    l.append(1);
    l.append(1);
    l.append(2);
    l.removeDups();

    LinkedList l12 = LinkedList();
    l12.append(1);
    l12.append(2);

    assert(l == l12);

    LinkedList ll = LinkedList();
    ll.append(1);
    ll.append(2);
    ll.append(1);
    ll.append(1);
    ll.append(2);
    ll.append(2);
    ll.removeDups();
    assert(ll == l12);

    LinkedList lll = LinkedList();
    lll.removeDups();
    LinkedList l_empty = LinkedList();
    assert(lll == l_empty);

    lll.append(1);
    lll.removeDups();
    LinkedList l1 = LinkedList();
    l1.append(1);
    assert(lll == l1);
}

void testRemoveDupsSlow()
{
    LinkedList l = LinkedList();
    l.append(1);
    l.append(1);
    l.append(1);
    l.append(1);
    l.append(2);
    l.removeDupsSlow();

    LinkedList l12 = LinkedList();
    l12.append(1);
    l12.append(2);

    assert(l == l12);

    LinkedList ll = LinkedList();
    ll.append(1);
    ll.append(2);
    ll.append(1);
    ll.append(1);
    ll.append(2);
    ll.append(2);
    ll.removeDupsSlow();
    assert(ll == l12);

    LinkedList lll = LinkedList();
    lll.removeDupsSlow();
    LinkedList l_empty = LinkedList();
    assert(lll == l_empty);

    lll.append(1);
    lll.removeDupsSlow();
    LinkedList l1 = LinkedList();
    l1.append(1);
    assert(lll == l1);
}
