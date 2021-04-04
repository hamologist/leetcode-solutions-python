function subsets(nums: number[]): number[][] {
  const vals: number[][] = [];
  (function inner (acc: number[], nums: number[]) {
    vals.push(acc);
    if (nums.length == 0) {
      return;
    }

    for (let i = 0; i < nums.length; i++) {
      inner(acc.concat(nums[i]), nums.filter((num: number, index: number) => index > i))
    }

  })([], nums);

  return vals;
}

console.log(subsets([1, 2, 3]));