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
 * @param {number} index
 * @return {number}
 */
DinnerPlates.prototype.popAtStack = function(index) {
	// Make sure the stack exists and is not empty.	
  if (this.stacks.length <= index || this.stacks[index].length == 0) {
    return -1;
  };
  this.insertOpenStack(index);
	return this.stacks[index].pop();
  };

/** 
 * @param {integer} index
 * @return {void}
 */
 DinnerPlates.prototype.insertOpenStack = function(index) {
	if (this.openStacks.length == 0) {
		this.openStacks.push(index);
	};
	for (let i = 0; i < this.openStacks.length; i++) {
		if (index < this.openStacks[i]) {
			this.openStacks.splice(i, 0, index);
			return;
		};
		if (index == this.openStacks[i]) {
			return;
		};
	};
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
