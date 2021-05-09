class LLNode {
  constructor(val, next) {
    this.val = val;
    this.next = next;
  }
}

class Queue {
  constructor() {
    this.head = null;
    this.tail = null;
  }
  enqueue(node) {
    if (this.head === null) {
      this.head = new LLNode(node, null);
      this.tail = this.head;
    } else {
      this.tail.next = new LLNode(node, null);
      this.tail = this.tail.next;
    }
  }
  isempty() {
    return this.head === null;
  }
  dequeue() {
    if (this.isempty()) {
      return undefined;
    }
    const answer = this.head.val;
    this.head = this.head.next;
    return answer;
  }
}

class GNode {
  constructor(val, adjacent) {
    this.val = val;
    this.adjacent = adjacent;
    this.marked = false;
  }
}

function BreadthFirstSearch(source, destination) {
  const queue = new Queue();
  source.marked = true;
  queue.enqueue(source);

  while (!queue.isempty()) {
    const current = queue.dequeue();
    for (let neighb of current.adjacent) {
      if (neighb === destination) {
        return true;
      }
      if (!neighb.marked) {
        neighb.marked = true;
        queue.enqueue(neighb);
      }
    }
  }
  return false;
}

function RouteBetweenNodes(n1, n2) {
  return BreadthFirstSearch(n1, n2) || BreadthFirstSearch(n2, n1);
}

/* Test Cases */

// Graph 1: {
//   a: ['a', 'b'],
//   b: ['c'],
//   c: ['d'],
//   d: ['b', 'c']
// }
const nodeA1 = new GNode('a', []);
const nodeB1 = new GNode('b', []);
const nodeC1 = new GNode('c', []);
const nodeD1 = new GNode('d', []);

nodeA1.adjacent.push(nodeA1, nodeB1)
nodeB1.adjacent.push(nodeC1)
nodeC1.adjacent.push(nodeD1)
nodeD1.adjacent.push(nodeB1, nodeC1)

console.log(RouteBetweenNodes(nodeA1, nodeD1), '=== true')

// Graph 2: {
//   a: ['a', 'b'],
//   b: [],
//   c: [],
//   d: ['b', 'c']
// }
const nodeA2 = new GNode('a', []);
const nodeB2 = new GNode('b', []);
const nodeC2 = new GNode('c', []);
const nodeD2 = new GNode('d', []);

nodeA2.adjacent.push(nodeA2, nodeB2)
nodeB2.adjacent.push()
nodeC2.adjacent.push()
nodeD2.adjacent.push(nodeB2, nodeC2)

console.log(RouteBetweenNodes(nodeA2, nodeD2), '=== false')

// Graph 3 {
//   a: ['a'],
//   b: [],
//   c: [],
//   d: ['b', 'c']
// }

const nodeA3 = new GNode('a', []);
const nodeB3 = new GNode('b', []);
const nodeC3 = new GNode('c', []);
const nodeD3 = new GNode('d', []);

nodeA3.adjacent.push(nodeA3, nodeB3)
nodeB3.adjacent.push()
nodeC3.adjacent.push()
nodeD3.adjacent.push(nodeB3, nodeC3)

console.log(RouteBetweenNodes(nodeA3, nodeD3), '=== false')

// const graph4 = {
//   a: [],
//   b: ['a'],
//   c: ['d'],
//   d: ['b', 'c']
// }

const nodeA4 = new GNode('a', []);
const nodeB4 = new GNode('b', []);
const nodeC4 = new GNode('c', []);
const nodeD4 = new GNode('d', []);

nodeB4.adjacent.push(nodeA4)
nodeC4.adjacent.push(nodeD4)
nodeD4.adjacent.push(nodeB4, nodeC4)

console.log(RouteBetweenNodes(nodeA4, nodeD4), '=== true')

// const graph5 = {
//   a: ['a'],
//   b: ['a'],
//   c: ['e'],
//   d: ['c'],
//   e: ['c', 'b'],
// }

const nodeA5 = new GNode('a', []);
const nodeB5 = new GNode('b', []);
const nodeC5 = new GNode('c', []);
const nodeD5 = new GNode('d', []);
const nodeE5 = new GNode('e', []);

nodeA5.adjacent.push(nodeA5)
nodeB5.adjacent.push(nodeA5)
nodeC5.adjacent.push(nodeE5)
nodeD5.adjacent.push(nodeC5)
nodeE5.adjacent.push(nodeB5, nodeC5)

console.log(RouteBetweenNodes(nodeA5, nodeD5), '=== true')

