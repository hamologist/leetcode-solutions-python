function containsDuplicate(nums: number[]): boolean {
  const lookup = new Map<number, boolean>();

  for (let num of nums) {
    if (lookup.has(num)) {
      return true;
    }

    lookup.set(num, true);
  }

  return false;
}

console.log(containsDuplicate([1, 2, 3, 1]))
console.log(containsDuplicate([1, 2, 3, 4]))
console.log(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))