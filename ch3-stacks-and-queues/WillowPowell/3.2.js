class MinStack {
    constructor() {
        this.stack = [];   
    };
};

/** 
 * @param {number} val
 * @return {void}
 */
MinStack.prototype.push = function(val) {
    this.stack.push({
        val: val,
        min: this.stack.length > 0 ? Math.min(val, this.stack[this.stack.length - 1].min) : val
    });
};

/**
 * @return {void}
 */
MinStack.prototype.pop = function() {
    this.stack.pop();
};

/**
 * @return {number}
 */
MinStack.prototype.top = function() {
    return this.stack[this.stack.length - 1].val;
};

/**
 * @return {number}
 */
MinStack.prototype.getMin = function() {
    return this.stack[this.stack.length - 1].min;
};

const obj = new MinStack();
obj.push(-2);
obj.push(0);
obj.push(-3);
console.log(obj.getMin(), "== -3");
obj.pop();
console.log(obj.top(), "== 0");
console.log(obj.getMin(), "== -2");
