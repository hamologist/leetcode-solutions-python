function fourSumCount(A: number[], B: number[], C: number[], D: number[]): number {
  const CDLookup = new Map<number, number>();
  let tupleCount = 0;

  for (let c of C) {
    for (let d of D) {
      CDLookup.set(c + d, (CDLookup.get(c + d) || 0) + 1);
    }
  }

  for (let a of A) {
    for (let b of B) {
      if (CDLookup.has(-(a + b))) {
        tupleCount += CDLookup.get(-(a + b)) as number;
      }
    }
  }

  return tupleCount;
}

console.log(fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))