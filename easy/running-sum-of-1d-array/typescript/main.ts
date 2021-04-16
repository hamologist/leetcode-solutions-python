function runningSum(nums: number[]): number[] {
  const run = new Array<number>(nums.length);
  let prev = 0;
  for (let i = 0; i < nums.length; i++) {
    run[i] = nums[i] + prev;
    prev = run[i];
  }

  return run;
}

console.log(runningSum([1, 2, 3, 4]));
console.log(runningSum([1, 1, 1, 1, 1]));
console.log(runningSum([3, 1, 2, 10, 1]));
