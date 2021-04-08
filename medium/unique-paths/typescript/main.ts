function uniquePaths(m: number, n: number): number {
  const lookup = new Map<string, number>();
  return (function inner(x: number, y: number): number {
    if (x >= n || y >= m) {
      return 0;
    }
    if (x == n - 1 && y == m - 1) {
      return 1;
    }
    let count = 0;
    if (lookup.has(`${x+1},${y}`)) {
      count += lookup.get(`${x+1},${y}`) as number
    } else {
      count += inner(x + 1, y);
    }

    if (lookup.has(`${x},${y+1}`)) {
      count += lookup.get(`${x},${y+1}`) as number
    } else {
      count += inner(x, y + 1);
    }

    lookup.set(`${x},${y}`, count);
    return count;
  })(0, 0)
}

console.log(uniquePaths(3, 7))
console.log(uniquePaths(3, 2))
console.log(uniquePaths(7, 3))
console.log(uniquePaths(3, 3))
console.log(uniquePaths(23, 12))
