const { BinaryTree } = require('./data-structures');

function firstCommonAncestor(root, n1, n2) {
  if (n1 === root || n2 === root) {
    return root;
  }
  const n1Location = root.left && BinaryTree.inOrderTraversal(root.left, (node) => node === n1) ? 'left' : 'right';
  const n2Location = root.left && BinaryTree.inOrderTraversal(root.left, (node) => node === n2) ? 'left' : 'right';
  if (n1Location !== n2Location) {
    return root;
  }
  return n1Location === 'left' ? firstCommonAncestor(root.left, n1, n2) : firstCommonAncestor(root.right, n1, n2);
}

const myRoot = new BinaryTree(0);
const nodes = BinaryTree.makeBalancedTree(3, myRoot);

console.log(firstCommonAncestor(myRoot, nodes[5], nodes[14]) === myRoot);
console.log(firstCommonAncestor(myRoot, nodes[0], nodes[4]) === myRoot);
console.log(firstCommonAncestor(myRoot, nodes[8], nodes[13]) === nodes[8]);
console.log(firstCommonAncestor(myRoot, nodes[10], nodes[13]) === nodes[8]);
nodes[8].left = null;
console.log(firstCommonAncestor(myRoot, nodes[5], nodes[14]) === myRoot);
console.log(firstCommonAncestor(myRoot, nodes[13], nodes[14]) === nodes[12]);
