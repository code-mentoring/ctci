const { Node, List } = require('./DoublyLinkedList');

class MyQueue extends List {
  enqueue(node) {
    this.insertEnd(node);
  }
  dequeue() {
    if (this.isEmpty()) {
      return;
    }
    return this.removeBeginning();
  }
  requeue(node) {
    this.remove(node);
    this.enqueue(node);
  }
}

class LeastRecentlyUsedCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.size = 0;
    this.cache = {
      // Example:
      // key: {
      //   Node(
      //     data: {
      //       key,
      //       val,
      //     prev, next
      //   )
      // }
    }
    this.queue = new MyQueue();
  }
  eject() {
    const ejected = this.queue.dequeue();
    delete this.cache[ejected.data.key];
    this.size -= 1;
    return;
  }
  get(key) {
    const node = this.cache[key];
    if (node === undefined) {
      return -1;
    }
    this.queue.requeue(node);
    return node.data.val;
  }
  put(key, val) {
    if (this.cache[key]) { // Won't need to eject if it exists.
      const node = this.cache[key];
      node.data.val = val;
      this.queue.requeue(node);
      return;
    }
    if (this.size === this.capacity) {
      this.eject();
    }
    const newNode = new Node({ key, val });
    this.queue.enqueue(newNode);
    this.cache[key] = newNode;
    this.size += 1;
  }
}

module.exports = LeastRecentlyUsedCache;
