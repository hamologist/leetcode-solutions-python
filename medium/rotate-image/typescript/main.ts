function rotate(matrix: number[][]): void {
  for (let y = 0; y < matrix.length; y++) {
    for (let x = y; x < matrix[y].length; x++) {
      const temp = matrix[x][y];
      matrix[x][y] = matrix[y][x];
      matrix[y][x] = temp;
    }
  }

  for (let y = 0; y < matrix.length; y++) {
    for (let x = 0; x < Math.floor(matrix[y].length / 2); x++) {
      const temp = matrix[y][x];
      const end = matrix[y].length - x - 1;
      matrix[y][x] = matrix[y][end];
      matrix[y][end] = temp;
    }
  }
}

(() => {
  let input = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
  ];
  rotate(input);
  console.log(input);

  input = [
    [1, 2],
    [3, 4],
  ]
  rotate(input);
  console.log(input);
})()
