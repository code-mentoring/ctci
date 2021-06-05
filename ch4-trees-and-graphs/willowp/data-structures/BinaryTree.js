class BinaryTree {
  constructor(val, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
  static inOrderTraversal(root, visit) {
    if (root !== null) {
      const left = BinaryTree.inOrderTraversal(root.left, visit);
      if (left === true) {
        return true;
      }
      const mid = visit(root);
      if (mid === true) {
        return true;
      }
      const right = BinaryTree.inOrderTraversal(root.right, visit);
      if (right === true) {
        return true;
      }
    }
    return false;
  }
  /* Helper for making test cases. */
  static makeBalancedTree(depth, root, arr = []) {
    arr.push(root);
    if (depth === 0) {
      return [arr];
    }
    const left = new BinaryTree(arr.length);
    root.left = left;
    BinaryTree.makeBalancedTree(depth - 1, left, arr);
    const right = new BinaryTree(arr.length);
    root.right = right;
    BinaryTree.makeBalancedTree(depth - 1, right, arr);
    return arr;
  }
  static bst(arr, parent = null) {
    if (arr.length === 0) {
      return null;
    }
    const mid = Math.floor(arr.length / 2);
    const root = new BinaryTree(arr[mid]);
    root.parent = parent;
    root.left = BinaryTree.bst(arr.slice(0, mid), root);
    root.right = BinaryTree.bst(arr.slice(mid + 1), root);
    return root;
  }
  static binarySearch(root, val) {
    if (root.val === val) {
      return root;
    }
    if (val < root.val) {
      return root.left && BinaryTree.binarySearch(root.left, val);
    }
    return root.right && BinaryTree.binarySearch(root.right, val);
  }
}

module.exports = BinaryTree;
