const SinglyLinkedList = require('./SinglyLinkedList');

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
  }
  enqueue(val) {
    const newNode = new SinglyLinkedList(val);
    if (this.head === null) {
      this.head = newNode;
      return;
    } else if (this.tail === null) {
      this.head.next = newNode;
    } else {
      this.tail.next = newNode;
    }
    this.tail = newNode;
  }
  dequeue() {
    if (this.head === null) {
      return undefined;
    }
    const answer = this.head.val;
    this.head = this.head.next;
    return answer;
  }
  isEmpty() {
    return this.head === null;
  }
}

module.exports = Queue;
