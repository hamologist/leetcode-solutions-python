function gameOfLife(board: number[][]): void {
  const memo = new Map<string, number>();

  function getNeighbor(x: number, y: number): number {
    const key = `${x},${y}`;
    const mem = memo.get(key);
    return mem !== undefined ? mem : board[y][x];
  }

  function getNeighbors(x: number, y: number): number {
    const aboveExists = y > 0;
    const belowExists = y < board.length - 1;
    const leftExists = x > 0;
    const rightExists = x < board[y].length - 1;
    let neighbors = 0;

    if (aboveExists) {
      neighbors += getNeighbor(x, y-1);

      if (leftExists) {
        neighbors += getNeighbor(x-1, y-1);
      }

      if (rightExists) {
        neighbors += getNeighbor(x+1, y-1);
      }
    }

    if (belowExists) {
      neighbors += getNeighbor(x, y+1);

      if (leftExists) {
        neighbors += getNeighbor(x-1, y+1);
      }

      if (rightExists) {
        neighbors += getNeighbor(x+1, y+1);
      }
    }

    if (leftExists) {
      neighbors += getNeighbor(x-1, y);
    }

    if (rightExists) {
      neighbors += getNeighbor(x+1, y);
    }

    return neighbors;
  }

  for (let y = 0; y < board.length; y++) {
    for (let x = 0; x < board[y].length; x++) {
      const current = board[y][x];
      const count = getNeighbors(x, y);
      memo.set(`${x},${y}`, current);

      if (current == 1) {
        if (count < 2 || count > 3) {
          board[y][x] = 0;
        }
      } else {
        if (count === 3) {
          board[y][x] = 1;
        }
      }
    }
  }
}

(() => {
  function printBoard(board: number[][]) {
    for (let y = 0; y < board.length; y++) {
      console.log(board[y]);
    }
  }

  let input = [
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
  ];
  gameOfLife(input);
  printBoard(input);
  console.log();

  input = [
    [1,1],
    [1,0]
  ];
  gameOfLife(input)
  printBoard(input);
})();