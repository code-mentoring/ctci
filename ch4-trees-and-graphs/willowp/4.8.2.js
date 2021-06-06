const { BinaryTree } = require('./data-structures');

function firstCommonAncestor(root, n1, n2) {
  let answer = null;

  function fca(node) {
    if (answer) {
      return;
    }
    if (!node) {
      return false;
    }
    const left = fca(node.left);
    const right = fca(node.right);
    const mid = node === n1 || node === n2;

    if ((left + right + mid) >= 2) {
      answer = node;
    }
    if (left || right || mid) {
      return true;
    }
    return false;
  }
  fca(root);
  return answer;
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
