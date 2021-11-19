from typing import Dict, List

from _shared.test import BaseTest


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        memo: Dict[tuple, int] = {}
        col_length = len(board)
        row_length = len(board[0])

        def _check(_y: int, _x: int) -> 0:
            if _x < 0 or _x >= row_length or _y < 0 or _y >= col_length:
                return 0

            if (_y, _x) in memo:
                return memo[(_y, _x)]

            return board[_y][_x]

        for y in range(0, len(board)):
            for x in range(0, len(board[y])):
                current = board[y][x]
                neighbors = (
                    _check(y - 1, x) + _check(y - 1, x - 1) + _check(y - 1, x + 1)
                    + _check(y + 1, x) + _check(y + 1, x - 1) + _check(y + 1, x + 1)
                    + _check(y, x - 1) + _check(y, x + 1)
                )
                if current == 1 and (neighbors < 2 or neighbors > 3):
                    board[y][x] = 0
                    memo[(y, x)] = 1
                elif current == 0 and neighbors == 3:
                    board[y][x] = 1
                    memo[(y, x)] = 0


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        _input = [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
            [0, 0, 0]
        ]
        self.solution.gameOfLife(_input)
        self.assertEqual(
            [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]],
            _input
        )

    def test_two(self):
        _input = [
            [1, 1],
            [1, 0]
        ]
        self.solution.gameOfLife(_input)
        self.assertEqual(
            [[1, 1], [1, 1]],
            _input
        )


if __name__ == '__main__':
    Test.execute()
