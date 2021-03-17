// Intersection; Given two (singly) linked lists, determine if the two lists intersect.
// Return the inter- secting node. Note that the intersection is defined based on reference, not value. 
// That is, if the kth node of the first linked list is the exact same node (by reference) as the j t h node 
// of the second linked list, then they are intersecting.

//constructor function 
class LinkedList {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
};

function peek(stack) {
    return stack[stack.length - 1]
};

function intersection(head1, head2) {
    let stack1 = [];
    let stack2 = [];

    while (head1 !== null) {
        stack1.push(head1);
        head1 = head1.next;
    }
    while (head2 !== null) {
        stack2.push(head2);
        head2 = head2.next;
    }

    //if not intersecting return undefined 
    if (stack1.length === 0 || stack2.length === 0) {
        return undefined;
    } else if (peek(stack1) !== peek(stack2)) {
        return undefined;
    } else {
        let intersect;
        while (peek(stack1) === peek(stack2)) {
            intersect = peek(stack1);
            stack1.pop();
            stack2.pop();
        }
        return intersect
    }
};

let a = new LinkedList('a');
let b = new LinkedList('b');
let c = new LinkedList('c');
let d = new LinkedList('d');
let e = new LinkedList('e');
let f = new LinkedList('f');
let g = new LinkedList('g');
let h = new LinkedList('h');

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
f.next = g;
g.next = h;

let a1 = new LinkedList('a1');
let b1 = new LinkedList('b1');
let c1 = new LinkedList('c1');

a1.next = b1;
b1.next = c1;
c1.next = d;

let intersectNode = intersection(a, a1);

console.log(intersectNode.value);