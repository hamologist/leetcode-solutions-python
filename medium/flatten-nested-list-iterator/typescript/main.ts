// This is the interface that allows for creating nested lists.
// You should not implement it, or speculate about its implementation
interface NestedInteger {
  // If value is provided, then it holds a single integer
  // Otherwise it holds an empty nested list
  constructor(value?: number): this;

  // Return true if this NestedInteger holds a single integer, rather than a nested list.
  isInteger(): boolean;

  // Return the single integer that this NestedInteger holds, if it holds a single integer
  // Return null if this NestedInteger holds a nested list
  getInteger(): number | null;

  // Set this NestedInteger to hold a single integer equal to value.
  setInteger(value: number): void;

  // Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
  add(elem: NestedInteger): void;

  // Return the nested list that this NestedInteger holds,
  // or an empty list if this NestedInteger holds a single integer
  getList(): NestedInteger[];
}

class NestedIterator {
  nestedList: NestedInteger[];
  current: number;
  child: NestedIterator | null;

  constructor(nestedList: NestedInteger[]) {
    this.nestedList = nestedList;
    this.current = -1;
    this.child = null;
  }

  hasNext(): boolean {
    const inner = (current: number): boolean => {
      if (this.child !== null && this.child.hasNext()) {
        return true;
      }

      if (current + 1 >= this.nestedList.length) {
        return false;
      }
      const next = this.nestedList[current + 1];
      if (next.isInteger()) {
        return true;
      }
      if (new NestedIterator(next.getList()).hasNext()) {
        return true;
      }

      return inner(current + 1);
    };

    return inner(this.current);
  }

  next(): number {
    const inner = (): number => {
      if (this.child !== null && this.child.hasNext()) {
        return this.child.next();
      }
      this.child = null;
      this.current++;

      const nestedInteger = this.nestedList[this.current];
      if (nestedInteger.isInteger()) {
        return nestedInteger.getInteger() as number;
      }
      this.child = new NestedIterator(nestedInteger.getList());
      return inner();
    }

    return inner();
  }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new NestedIterator(nestedList)
 * var a: number[] = []
 * while (obj.hasNext()) a.push(obj.next());
 */