function majorityElement(nums: number[]): number {
  const lookup = new Map<number, number>();
  let largestNum: number = 0;
  let largestCount: number = 0;
  for (let num of nums) {
    const currentCount = (lookup.get(num) || 0) + 1;
    lookup.set(num, currentCount);

    if (currentCount > largestCount) {
      largestNum = num;
      largestCount = currentCount;
    }
  }

  return largestNum
}

console.log(majorityElement([3, 2, 3]))
console.log(majorityElement([2, 2, 1, 1, 1, 2, 2]))
