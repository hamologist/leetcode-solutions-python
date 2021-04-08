function generate(numRows: number): number[][] {
  const nums = new Array<Array<number>>([1]);
  for (let i = 1; i < numRows; i++) {
    const row = new Array<number>(i + 1);
    for (let j = 0; j < i + 1; j++) {
      row[j] = (nums[i - 1][j - 1] || 0) + (nums[i - 1][j] || 0)
    }
    nums.push(row);
  }

  return nums;
}

console.log(generate(5))
console.log(generate(1))
