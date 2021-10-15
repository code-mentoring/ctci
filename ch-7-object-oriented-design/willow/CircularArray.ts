class CircularArray<Type> {
  list;
  startIndex;
  constructor(...args: Array<Type>) {
    this.list = args;
    this.startIndex = 0;
    // Commented out attempt to make indexable like myCircArr[2]
    // Worked before we added TypeScript :|
    // return new Proxy(this, {
    //   get: function(obj: CircularArray<Type>, target: keyof CircularArray<Type> | number): Type | void{
    //     if (Number.isInteger(Number(String(target)))) {
    //       return obj.list[Number(target) + obj.startIndex]
    //     }
    //     return obj[target]
    //   }
    // })
  }

  [Symbol.iterator]() {
    let i = this.startIndex;
    const arr = this.list;
    return {
      next(): {
        done: boolean,
        value?: Type
      } {
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

  // Rotate left by n steps.
  rotate(n: number): void {
    let i = 0;
    while (i < n) {
      const el = this.list[this.startIndex];
      delete this.list[this.startIndex];
      this.list.push(el);
      this.startIndex ++;
      i ++;
    }
  }

  push(...args:Array<Type>): void {
    for (let i = 0; i < args.length; i++) {
      this.list.push(args[i])
    }
  }

  pop(): Type | undefined {
    return this.list.pop();
  }

  get length() { return this.list.length - this.startIndex }

  get(i: number): Type {
    return this.list[i + this.startIndex];
  }
}
