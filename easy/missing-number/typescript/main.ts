function missingNumber(nums: number[]): number {
  const sum = nums.reduce((acc, current) => acc + current)
  const expected = ((nums.length + 1) * nums.length) / 2;

  return expected - sum;
}

console.log(missingNumber([3, 0, 1]))
console.log(missingNumber([0, 1]))
console.log(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
console.log(missingNumber([0]))
