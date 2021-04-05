function moveZeroes(nums: number[]): void {
  let i = 0;
  let count = 0;

  while (count < nums.length) {
    if (nums[i] == 0) {
      nums.splice(i, 1);
      nums.push(0);
    } else {
      i++;
    }
    count++
  }
}

(() => {
  let input = [0, 1, 0, 3, 12];
  moveZeroes(input);
  console.log(input)
  console.log();

  input = [0];
  moveZeroes(input);
  console.log(input);
})()