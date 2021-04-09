class Solution {
  original: number[];
  nums: number[];

  constructor(nums: number[]) {
    this.original = [...nums];
    this.nums = nums;
  }

  reset(): number[] {
    return this.nums = [...this.original];
  }

  shuffle(): number[] {
    for (let i = this.nums.length - 1; i > 0; i--) {
      const temp = this.nums[i];
      const randPos = Math.floor(Math.random() * (i + 1))
      this.nums[i] = this.nums[randPos];
      this.nums[randPos] = temp;
    }

    return this.nums;
  }
}

const solution = new Solution([1, 2, 3])
console.log(solution.shuffle())
console.log(solution.reset())
console.log(solution.shuffle())
console.log(solution.reset())
console.log(solution.shuffle())
console.log(solution.reset())
console.log(solution.shuffle())
console.log(solution.reset())
console.log(solution.shuffle())
