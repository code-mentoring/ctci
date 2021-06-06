const {BinaryTree} = require('./data-structures');

function sequences(root) {
  let answer = [];
  if (!root) {
    return answer;
  }
  answer.push([root.val]);
  addChildren(root);

  function addChildren(node) {
    // Add the children...
    if (node.left) {
      addChild(node, node.left);
    }
    if (node.right) {
      addChild(node, node.right);
    }
    // And then add the children's children.
    if (node.left) {
      addChildren(node.left);
    }
    if (node.right) {
      addChildren(node.right);
    }
  }

  function addChild(parent, child) {
    // For each existing sequence...
    answer = answer.reduce((answerAcc, sequence) => {
      // Find the index of the parent...
      const parentIndex = sequence.indexOf(parent.val);
      // For every index after the parent...
      for (let i = parentIndex; i < sequence.length; i++) {
        // Insert the new value.
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

const n1 = new BinaryTree(1);
const n2 = new BinaryTree(2);
const n4 = new BinaryTree(4);
const n5 = new BinaryTree(5);
const n8 = new BinaryTree(8);

n5.left = n2;
n5.right = n8;
n2.left = n1;
n2.right = n4;

const answerN = sequences(n5);
console.log(sequences(n5));
console.log([
  [5,8,2,4,1],
  [5,8,2,1,4],
  [5,2,4,1,8],
  [5,2,1,4,8],
  [5,2,1,8,4],
  [5,2,4,8,1],
  [5,2,8,4,1],
  [5,2,8,1,4],
].every((s, i) => {
  return s.every((el, j) => {
    return el === answerN[i][j];
  });
}));

const m1 = new BinaryTree(1);
const m2 = new BinaryTree(2);
const m4 = new BinaryTree(4);
const m5 = new BinaryTree(5);
const m8 = new BinaryTree(8);

m1.right=m2
m2.right=m4
m4.right=m5
m5.right=m8

console.log(sequences(m1));

const o1 = new BinaryTree(1);
const o2 = new BinaryTree(2);
const o4 = new BinaryTree(4);
const o5 = new BinaryTree(5);
const o8 = new BinaryTree(8);

o8.left=o5
o5.left=o4
o4.left=o2
o2.left=o1


console.log(sequences(o8));

const p1 = new BinaryTree(1);
const p2 = new BinaryTree(2);
const p4 = new BinaryTree(4);
const p5 = new BinaryTree(5);
const p8 = new BinaryTree(8);

p1.right=p2
p2.right=p5
p5.left=p4
p5.right=p8

console.log(sequences(p1));
