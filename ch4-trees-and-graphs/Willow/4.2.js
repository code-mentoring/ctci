class Node {
  constructor(val, left, right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

function MinimalTree(arr) {
  if (arr.length === 0) {
    return null;
  }
  if (arr.length === 1) {
    return new Node(arr[0], null, null);
  }
  const centreIndex = Math.floor(arr.length / 2);
  const root = new Node(
    arr[centreIndex],
    MinimalTree(arr.slice(0, centreIndex)),
    MinimalTree(arr.slice(centreIndex + 1))
  )
  return root;
}

console.log(JSON.stringify(MinimalTree([1, 2, 3, 3, 4]), null, 2))
