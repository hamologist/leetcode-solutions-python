function maxArea(height: number[]): number {
  let leftPtr = 0;
  let rightPtr = height.length - 1;
  let max = 0;

  while (leftPtr !== rightPtr) {
    max = Math.max(max, Math.min(height[leftPtr], height[rightPtr]) * (rightPtr - leftPtr));
    if (height[leftPtr] < height[rightPtr]) {
      leftPtr += 1;
    } else {
      rightPtr -= 1;
    }
  }

  return max;
}

console.log(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]));
console.log(maxArea([1, 1]));
console.log(maxArea([4, 3, 2, 1, 4]));
console.log(maxArea([1, 2, 1]));
