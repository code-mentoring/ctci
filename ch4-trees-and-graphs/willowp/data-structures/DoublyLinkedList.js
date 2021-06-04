class Node {
  constructor(data) {
    this.data = data;
    this.prev = null;
    this.next = null;
  }
}

class List {
  constructor() {
    const head = new Node(null);
    const tail = new Node(null);
    tail.prev = head;
    head.next = tail;
    this.head = head;
    this.tail = tail;
  }
  insertAfter(node, newNode) {
    newNode.prev = node;
    newNode.next = node.next;
    node.next.prev = newNode;
    node.next = newNode;
  }
  insertBefore(node, newNode) {
    newNode.next = node;
    newNode.prev = node.prev;
    node.prev.next = newNode;
    node.prev = newNode;
  }
  insertBeginning(newNode) {
    this.insertBefore(this.head.next, newNode);
  }
  insertEnd(newNode) {
    this.insertAfter(this.tail.prev, newNode);
  }
  isEmpty() {
    return this.head.next === this.tail;
  }
  remove(node) {
    node.prev.next = node.next;
    node.next.prev = node.prev;
    node.next = null;
    node.prev = null;
    return node;
  }
  removeBeginning() {
    if (this.isEmpty()) {
      return;
    }
    return this.remove(this.head.next);
  }
  removeEnd() {
    if (this.isEmpty()) {
      return;
    }
    return remove(this.tail.prev);
  }
}

module.exports = { Node, List };
