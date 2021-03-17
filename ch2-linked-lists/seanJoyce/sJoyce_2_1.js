// Remove Dups: Write code to remove duplicates from an unsorted linked list.
// FOLLOW UP How would you solve this problem if a temporary buffer is not allowed?

'use strict'

// User defined class node 
class Node {
    // Constructor
    constructor(data) {
        this.data = data; // Data of node
        this.next = null; // Points to an empty next node
    }
}

// linkedlist class 
class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    head() {
        return this.head;
    }

    tail() {
        return this.tail;
    }

    append(data) {
        let node = new Node(data);
        //if list is empty
        if (!this.head) {
            this.head = node;
            this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
    }

    prepend(data) {
        let node = new Node(data);
        node.next = this.head;
        this.head = node;
    }

    pop() {
        let current = this.head;
        // only one or no item exists
        if (!current) {
            return null;
        } else if (!current.next) {
            this.head = null;
            return current
        }
        // move till the 2nd last
        while (current.next.next) {
            current = current.next;
        }
        let last = current.next;
        this.tail = current;
        this.tail.next = null;
        return last;
    }

    popFirst() {
        let first = this.head;
        if (this.head && this.head.next) {
            this.head = this.head.next;
            first.next = null;
        } else {
            this.head = null;
        }
        return first;
    }

    removeAt(index) {

    }

    _toArray() {
        let myArray = [];
        let current = this.head;
        while (current) {
            myArray.push(current.data)
            current = current.next;
        }
        return myArray;
    }


}

let list = new LinkedList();
for (let elem of [1, 5, 1, 6, 8, 6, 8, 8, 8, 8]) {
    list.append(elem);
}
list.prepend(5)
console.log(list._toArray())

