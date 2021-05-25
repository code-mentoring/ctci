const { BinaryTree } = require('./data-structures');

function minimalTree(arr) {
  if (arr.length === 0) {
    return null;
  }
  if (arr.length === 1) {
    return new BinaryTree(arr[0], null, null);
  }
  const centreIndex = Math.floor(arr.length / 2);
  const root = new BinaryTree(
    arr[centreIndex],
    minimalTree(arr.slice(0, centreIndex)),
    minimalTree(arr.slice(centreIndex + 1))
  )
  return root;
}

console.log(JSON.stringify(minimalTree([1, 2, 3, 3, 4]), null, 2))
