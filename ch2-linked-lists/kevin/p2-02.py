from linkedlist import *

def kth_last(ll, k):
    # First, find the node k steps from the head
    # of the list.
    k_ahead = ll.head
    while k_ahead and k > 0:
        k_ahead = k_ahead.next_node
        k -= 1
    if k > 0 and not k_ahead:
        # There aren't even k nodes in the list!
        return None
    # Second, step through the list until the k-ahead 
    # node falls off the end. That's how we know we're
    # k from the end.
    curr = ll.head
    while curr and k_ahead:
        curr = curr.next_node
        k_ahead = k_ahead.next_node
    return curr

def main():
    cases = [
        (make_list(1, 2, 3), 1, 3),
        (make_list(1, 2, 3), 2, 2),
        (make_list(1, 2, 3), 3, 1),
        (make_list(1, 2, 3), 4, None),
        (make_list(1), 1, 1),
        (make_list(1), 2, None),
        (make_list(), 1, None)
    ]
    for (ll, k, expected) in cases:
        result = kth_last(ll, k)
        success = ((result is None and expected is None)
            or (result is not None
                and result.value == expected))
        print(success, ll, k, result and result.value)

if __name__ == "__main__":
    main()
