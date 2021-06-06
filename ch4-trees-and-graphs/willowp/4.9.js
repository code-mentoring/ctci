const {BinaryTree} = require('./data-structures');

function sequences(root, answer = []) {
  if (!root) {
    return answer;
  }
  answer.push([root.val]);
  addChildren(root);

  function addChildren(node) {
    if (node.left) {
      addChild(node, node.left);
      addChildren(node.left);
    }
    if (node.right) {
      addChild(node, node.right);
      addChildren(node.right);
    }
  }

  function addChild(node, child) {
    answer = answer.reduce((answerAcc, sequence) => {
      const nodeIndex = sequence.indexOf(node.val);
      for (let i = nodeIndex; i < sequence.length; i++) {
        answerAcc.push([
          ...sequence.slice(0, i + 1),
          child.val,
          ...sequence.slice(i + 1),
        ]);
      }
      return answerAcc;
    }, []);
  }

  return answer;
}

// Test tree #1
const a = [0, 1, 2, 3, 4]
const root = BinaryTree.bst(a);
console.log(sequences(root));

// Test tree #1
const b = [0, 1, 2, 3, 4, 5]
const boot = BinaryTree.bst(b);
console.log(sequences(boot));
