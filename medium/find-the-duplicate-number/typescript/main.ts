function findDuplicate(nums: number[]): number {
  const lookup = new Map<number, boolean>();
  let dupe = 0;
  for (let num of nums) {
    const count = lookup.get(num) || false;

    if (count) {
      dupe = num;
      break;
    }
    lookup.set(num, true)
  }

  return dupe;
}

console.log(findDuplicate([1, 3, 4, 2, 2]));
console.log(findDuplicate([3, 1, 3, 4, 2]));
console.log(findDuplicate([1, 1]));
console.log(findDuplicate([1, 1, 2]));