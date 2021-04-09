function hammingWeight(n: number): number {
  let count = 0;

  while (n !== 0) {
    count += n % 2;
    n = n >>> 1;
  }
  return count;
}

console.log(hammingWeight(parseInt("00000000000000000000000000001011", 2)))
console.log(hammingWeight(parseInt("00000000000000000000000010000000", 2)))
console.log(hammingWeight(parseInt("11111111111111111111111111111101", 2)))
