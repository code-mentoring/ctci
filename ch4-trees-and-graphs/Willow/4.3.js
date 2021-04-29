class LLNode {
  constructor(val, next) {
    this.type = "Linked List"
    this.val = val;
    this.next = next;
  }
}

class BTNode {
  constructor(val, left, right) {
    this.type = "Binary Tree"
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function listOfDepths(root) {
  if (root === null) {
    return null;
  }

  // Return a linked list of the children of a single BTNode.
  function singleNodeList(node) {
    let result = null;
    if (node.left !== null) {
      result = new LLNode(node.left, null);
    }
    if (node.right !== null) {
      let rightNode = new LLNode(node.right, null);
      if (result) {
        result.next = rightNode;
      } else {
        result = rightNode;
      }
    }
    return result;
  }

  // Return a linked list of all children of a linked list of BT nodes.
  function listOfChildren(head) {
    let result = null;
    let current = head; // The LLNode whose val (a BTNode) is being processed.
    let tail = null; // The most recently added LLNode.
    while (current !== null) {
      // Only add anything if there's a left or right node.
      if (current.val.left || current.val.right) {
        if (!result) {
          result = singleNodeList(current.val);
          tail = result.next ? result.next : result;
        } else {
          tail.next = singleNodeList(current.val);
          tail = tail.next.next ? tail.next.next : tail.next;
        }
      }
      current = current.next;
    }
    return result;
  }

  const lists = [new LLNode(root, null)];
  let nextList = listOfChildren(lists[0]);
  while (nextList) {
    lists.push(nextList);
    nextList = listOfChildren(nextList);
  }
  return lists;
}

console.log(JSON.stringify(listOfDepths(new BTNode(
  1,
  new BTNode(2,
    new BTNode(4, null, null),
    new BTNode(5, null, null)),
  new BTNode(3,
    new BTNode(6, null, null),
    new BTNode(7, null, null))
)), null, 2));
console.log(JSON.stringify(listOfDepths(new BTNode(
  1,
  new BTNode(2,
    null,
    new BTNode(5, null, null)),
  new BTNode(3,
    new BTNode(6, new BTNode(6.5, null, null), null),
    new BTNode(7, null, null))
)), null, 2));
