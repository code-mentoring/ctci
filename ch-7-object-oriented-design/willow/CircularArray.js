class CircularArray {
  constructor(...args) {
    this.list = args;
    this.startIndex = 0;
    return new Proxy(this, {
      get: function(obj, target){
        if (Number.isInteger(Number(String(target)))) {
          return obj.list[Number(target) + obj.startIndex]
        }
        return obj[target]
      }
    })
  }
  [Symbol.iterator] () {
    let i = this.startIndex;
    const arr = this.list;
    return {
      next() {
        if (i < arr.length) {
          const answer = {
            done: false,
            value: arr[i]
          }
          i ++;
          return answer;
        }
        return { done: true }
      }
    }
  }
  rotate(n){
    let i = 0;
    while (i < n) {
      const el = this.list[this.startIndex];
      delete this.list[this.startIndex];
      this.list.push(el);
      this.startIndex ++;
      i ++;
    }
  }
  get length() { return this.list.length - this.startIndex }
}

c = new CircularArray(1,2,3)
console.log([...c])
console.log(c[2])
c.rotate(1)
console.log(c[2])
console.log(c.length)
for(let i of c){console.log(i)}
