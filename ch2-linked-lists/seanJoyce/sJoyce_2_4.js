// Partition: Write code to partition a linked list around a value x,
// such that all nodes less than x come before all nodes greater than or equal to x. 
// If x is contained within the list, the values of x only need to be after the elements less than x (see below). 
// The partition element x can appear anywhere in the "right partition"; it does not need to appear between the 
// left and right partitions. 

// EXAMPLE Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5] Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

//create linked list
let LinkedList = function (value) {
    this.value = value;
    this.next = null;
};

let partition = function (head, partition) {
    let left;
    let middle;
    let right;
    let currLeft = null;
    let currMiddle = null;
    let currRight = null;

    let node = head;
    //pointer through nodes
    while (node !== null) {
        if (node.value < partition) {
            if (currLeft === null) {
                left = node;
                currLeft = left;
            } else {
                currLeft.next = node;
                currLeft.next = currLeft;
            }
        } else if (node.value > partition) {
            if (currRight === null) {
                right = node;
                currRight = right;
            } else {
                currRight.next = node;
                currRight.next = currRight;
            }
        } else {
            if (currMiddle === null) {
                middle = node;
                currMiddle = middle;
            } else {
                currMiddle.next = node;
                currMiddle.next = currMiddle;
            }
        }
        node = node.next;
    }
    currRight.next = null;
    // connect the left values with those matching the partition value
    currLeft.next = middle;
    // connect the middle with the right partitions
    currMiddle.next = right;
    // return head of new linkedList
    return left;
}

//print list 
let printList = function (a) {
    while (a !== null) {
        console.log(a.value);
        a = a.next;
    }
};

//create newly linked list 
let a = new LinkedList(3);
let b = new LinkedList(5);
let c = new LinkedList(8);
let d = new LinkedList(5);
let e = new LinkedList(10);
let f = new LinkedList(2);
let g = new LinkedList(1);

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;
f.next = g;

//create partitioned list 
let newa = partition(a, 5);
printList(newa);