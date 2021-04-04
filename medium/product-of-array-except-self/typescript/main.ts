function productExceptSelf(nums: number[]): number[] {
  let zeroCount = 0;
  const all = nums.reduce((acc, current) => {
    if (current === 0) {
      zeroCount++;
      return acc;
    }
    return acc * current
  }, 1)

  return nums.map(current => {
    if (current === 0 && zeroCount == 1) {
      return all
    }
    if (zeroCount > 0) {
      return 0;
    }

    return all / current;
  })
}

console.log(productExceptSelf([1, 2, 3, 4]));
console.log(productExceptSelf([-1,1,0,-3,3]));
