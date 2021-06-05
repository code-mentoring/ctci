const { BinaryTree } = require('./data-structures');

function successor(node) {
  if (node.right) {
    return leftmostChild(node.right) || node.right;
  }
  return findNextParent(node);
}

function leftmostChild(node) {
  if (!node.left) {
    return null;
  }
  return findLeftmost(node.left);
}

function findLeftmost(node) {
  if (node.left) {
    return findLeftmost(node.left);
  }
  return node;
}

function findNextParent(node) {
  if (!node.parent) {
    return null;
  }
  if (node.parent.val > node.val) {
    return node.parent;
  }
  return findNextParent(node.parent);
}

// Test tree #1
const a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
const root = BinaryTree.bst(a);
const arr = Object.values(a).map((num) => BinaryTree.binarySearch(root, num));
arr.forEach((node, i) => {
  const expected = arr[i + 1] || null;
  const result = successor(node);
  console.log(result === expected);
});

// Test tree #2
const b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
const boot = BinaryTree.bst(b);
const brr = Object.values(b).map((num) => BinaryTree.binarySearch(boot, num));
brr.forEach((node, i) => {
  const expected = brr[i + 1] || null;
  const result = successor(node);
  console.log(result === expected);
});
