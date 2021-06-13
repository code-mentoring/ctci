class ChaosTree {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
    this.nodesLeft = 0;
    this.nodesRight = 0;
  }
  get totalNodes() {
    return this.nodesLeft + this.nodesRight + 1;
  }
  get totalSlots() {
    return this.totalNodes + 1;
  }
  get slotsLeft() {
    return this.nodesLeft + 1;
  }
  get slotsRight() {
    return this.nodesRight + 1;
  }
  insert(val) {
    const newNode = new ChaosTree(val);

    function recurse(root) {
      const left = root.slotsLeft/root.totalSlots;
      const right = root.slotsRight/root.totalSlots;
      const direction = ChaosTree.weightedRandom(left, right);
      if (direction === 0) {
        root.nodesLeft += 1;
        if (!root.left) {
          root.left = newNode;
          return newNode;
        }
        return recurse(root.left);
      }
      root.nodesRight += 1;
      if (!root.right) {
        root.right = newNode;
        return newNode
      }
      return recurse(root.right);
    }

    return recurse(this);
  }

  delete() {
    if (!this.left && !this.right) {
      if (ChaosTree.weightedRandom(0.5,0.5) === 0) {
        throw new Error("Hey, ain't no nodes left to delete. You can't just delete a root that has no children. There will be no tree left. If you really wanna do that, maybe just go `delete chaos`. Wowza.");
      }
      this.val = "You messed up";
      this.left = undefined;
      this.right = undefined;
      this.nodesLeft = undefined;
      this.nodesRight = undefined;
      return this;
    }

    const that = this;

    function promote(heir, parent, ancestor) {
      if (heir === parent.left) {
        heir.nodesRight += parent.nodesRight;
        let slot = heir;
        while (slot.right !== null) {
          slot = slot.right;
          slot.nodesRight += parent.nodesRight;
        }
        slot.right = parent.right;
      } else {
        heir.nodesLeft += parent.nodesLeft;
        let slot = heir;
        while (slot.left !== null) {
          slot = slot.left;
          slot.nodesLeft += parent.nodesLeft;
        }
        slot.left = parent.left;
      }
      if (ancestor !== undefined) {
        if (parent === ancestor.left) {
          ancestor.left = heir;
        } else {
          ancestor.right = heir;
        }
      }
      if (parent === that) {
        that.val = heir.val;
        that.left = heir.left;
        that.right = heir.right;
        that.nodesLeft = heir.nodesLeft;
        that.nodesRight = heir.nodesRight;
      }
    }

    function recurse(node, parent) {
      const itsMe = 1/node.totalNodes;
      const left = node.nodesLeft/node.totalNodes;
      const right = node.nodesRight/node.totalNodes;
      const direction = ChaosTree.weightedRandom(itsMe, left, right);
      if (direction === 0) {
        const heir = node.left || node.right;
        if (heir === null) {
          if (parent.left === node) {
            parent.left = null;
          }
          if (parent.right === node) {
            parent.right = null;
          }
          return node;
        }
        let answer = node;
        if (node === that) {
          answer = new ChaosTree(that.val);
          answer.left = that.left;
          answer.right = that.right;
          answer.nodesLeft = that.nodesLeft;
          answer.nodesRight = that.nodesRight;
          answer.secret = "You got the root! Be careful with this."
        }
        promote(heir, node, parent);
        return answer;
      }
      if (direction === 1) {
        node.nodesLeft -= 1;
        return recurse(node.left, node);
      }
      node.nodesRight -= 1;
      return recurse(node.right, node);
    }

    return recurse(this);
  }

  getRandomNode() {
    const itsMe = 1/this.totalNodes;
    const left = this.nodesLeft/this.totalNodes;
    const right = this.nodesRight/this.totalNodes;
    const direction = ChaosTree.weightedRandom(itsMe, left, right);
    if (direction === 0) {
      return this;
    }
    if (direction === 1) {
      return this.left.getRandomNode();
    }
    return this.right.getRandomNode();
  }

  static weightedRandom(...args) {
    const percentages = args.map((x) => x * 100);
    const n = Math.floor(Math.random() * 100);
    let i = 0;
    let sum = 0;
    while (n >= percentages[i] + sum) {
      sum += percentages[i];
      i ++;
    }
    return i;
  }
}

module.exports = ChaosTree;
