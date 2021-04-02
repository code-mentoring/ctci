/**
 * @param {number} capacity
 */
class DinnerPlates {
	constructor(capacity) {
    this.capacity = capacity;
    this.stacks = [[]];
    // Array of the indices of stacks with space for more data.
    // This should remain sorted in ascending order to enable this.push to work properly.
    this.openStacks = [0]; 
	};
};

/** 
 * @param {number} val
 * @return {void}
 */
DinnerPlates.prototype.push = function(val) {
  if (this.openStacks.length == 0) {
    this.stacks.push([]);
    this.openStacks.push(this.stacks.length - 1);
  };
  // Push to the leftmost open stack.
  this.stacks[this.openStacks[0]].push(val);
  // If the stack is now full, remove it from openStacks.
  if (this.stacks[this.openStacks[0]].length == this.capacity) {
    this.openStacks.shift();
  };
};

/**
 * Recursive function that makes sure the collection is poppable before popping.
 * @return {number}
 */
DinnerPlates.prototype.pop = function() {
  // Null case.
  if (this.stacks.length == 1 && this.stacks[0].length == 0) {
      return -1;
  };
  // If the right stack is empty,
  // remove it and its entry in openStacks,
  // and recurse.
  if (this.stacks[this.stacks.length - 1].length == 0) {
    this.stacks.pop();
    this.openStacks.pop();
    return this.pop();
  };
  // Update openStacks first.
  if (this.openStacks[this.openStacks.length - 1] != this.stacks.length - 1) {
   this.openStacks.push(this.stacks.length - 1);
  };
  return this.stacks[this.stacks.length - 1].pop();
};

/**
 * Runs in O(n) time at worst case, since it would need to iterate the
 * @param {number} index
 * @return {number}
 */
DinnerPlates.prototype.popAtStack = function(index) {
	// Make sure the stack exists and is not empty.	
  if (this.stacks.length <= index || this.stacks[index].length == 0) {
    return -1;
  };
  this.openStacks = this.insertOpenStack(index, this.openStacks);
	return this.stacks[index].pop();
  };

/* Use binary search to insert index at the correct place in openStacks in O(log n) time. */
DinnerPlates.prototype.insertOpenStack = function(index, openStacks) {
	// Base cases.
	if (openStacks.length == 0) {
		openStacks.push(index);
		return openStacks;
	};
	if (index == openStacks[0] || index == openStacks[openStacks.length - 1]) {
		return openStacks;
	};
	if (index < openStacks[0]) {
		openStacks.unshift(index);
		return openStacks;
	};
	if (index > openStacks[openStacks.length - 1]) {
		openStacks.push(index);
		return openStacks;
	};

	// Divide in two and recurse on the half that the index belongs in.
	const middle = Math.floor(openStacks.length / 2);
	const leftNode = openStacks.slice(0, middle);
	const rightNode = openStacks.slice(middle);
	if (index <= leftNode[leftNode.length - 1]) {
		return this.insertOpenStack(index, leftNode).concat(rightNode);
	};
	return leftNode.concat(this.insertOpenStack(index, rightNode));
};

// Helpers for HTML page.
let obj = null;
function start(event) {
	event.preventDefault();
	const capacity = Number(document.getElementById("capacity").value);
	obj = new DinnerPlates(capacity);
	console.log(obj);
};
function push(event) {
	event.preventDefault();
	const val = Number(document.getElementById("push-val").value);
	obj.push(val);
	console.log(obj);
};
function pop(event) {
	event.preventDefault();
	console.log(obj.pop());
	console.log(obj);
};
function popAtStack(event) {
	event.preventDefault();
	const stack = Number(document.getElementById("popAtStack-val").value);
	console.log(obj.popAtStack(stack));
	console.log(obj);
};
