const { BinaryTree, SinglyLinkedList } = require('./data-structures');

function listOfDepths(root) {
  if (root === null) {
    return null;
  }

  // Return a linked list of the children of a single BinaryTree.
  function singleNodeList(node) {
    let result = null;
    if (node.left !== null) {
      result = new SinglyLinkedList(node.left, null);
    }
    if (node.right !== null) {
      let rightNode = new SinglyLinkedList(node.right, null);
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
    let current = head; // The SinglyLinkedList whose val (a BinaryTree) is being processed.
    let tail = null; // The most recently added SinglyLinkedList.
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

  const lists = [new SinglyLinkedList(root, null)];
  let nextList = listOfChildren(lists[0]);
  while (nextList) {
    lists.push(nextList);
    nextList = listOfChildren(nextList);
  }
  return lists;
}

console.log(JSON.stringify(listOfDepths(new BinaryTree(
  1,
  new BinaryTree(2,
    new BinaryTree(4, null, null),
    new BinaryTree(5, null, null)),
  new BinaryTree(3,
    new BinaryTree(6, null, null),
    new BinaryTree(7, null, null))
)), null, 2));
console.log(JSON.stringify(listOfDepths(new BinaryTree(
  1,
  new BinaryTree(2,
    null,
    new BinaryTree(5, null, null)),
  new BinaryTree(3,
    new BinaryTree(6, new BinaryTree(6.5, null, null), null),
    new BinaryTree(7, null, null))
)), null, 2));
