from collections import deque
from typing import Deque

from _shared.test import BaseTest


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        pacific = set()
        atlantic = set()
        res = []
        y_length = len(heights)
        x_length = len(heights[0])

        def bfs(_y: int, _x: int, _ocean: set):
            queue: Deque[(int, int, int)] = deque([(_y, _x, -1)])

            while queue:
                (__y, __x, _prev) = queue.popleft()

                if (__y < 0 or __x < 0 or __y >= y_length or __x >= x_length
                        or (__y, __x) in _ocean
                        or _prev > heights[__y][__x]):
                    continue

                _ocean.add((__y, __x))
                queue.append((__y - 1, __x, heights[__y][__x]))
                queue.append((__y + 1, __x, heights[__y][__x]))
                queue.append((__y, __x - 1, heights[__y][__x]))
                queue.append((__y, __x + 1, heights[__y][__x]))

        for y in range(0, y_length):
            bfs(y, 0, pacific)
            bfs(y, x_length - 1, atlantic)

        for x in range(0, x_length):
            bfs(0, x, pacific)
            bfs(y_length - 1, x, atlantic)

        for y in range(0, y_length):
            for x in range(0, x_length):
                if (y, x) in pacific and (y, x) in atlantic:
                    res.append([y, x])

        return res

    def pacificAtlanticWithDfs(self, heights: list[list[int]]) -> list[list[int]]:
        pacific = set()
        atlantic = set()
        res = []
        y_length = len(heights)
        x_length = len(heights[0])

        def dfs(_y: int, _x: int, _prev: int, _ocean: set):
            if (_y < 0 or _x < 0 or _y >= y_length or _x >= x_length
                    or (_y, _x) in _ocean
                    or _prev > heights[_y][_x]):
                return

            _ocean.add((_y, _x))
            dfs(_y - 1, _x, heights[_y][_x], _ocean)
            dfs(_y + 1, _x, heights[_y][_x], _ocean)
            dfs(_y, _x - 1, heights[_y][_x], _ocean)
            dfs(_y, _x + 1, heights[_y][_x], _ocean)

        for y in range(0, y_length):
            dfs(y, 0, -1, pacific)
            dfs(y, x_length - 1, -1, atlantic)

        for x in range(0, x_length):
            dfs(0, x, -1, pacific)
            dfs(y_length - 1, x, -1, atlantic)

        for y in range(0, y_length):
            for x in range(0, x_length):
                if (y, x) in pacific and (y, x) in atlantic:
                    res.append([y, x])

        return res


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
            self.solution.pacificAtlantic([
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ])
        )

    def test_two(self):
        self.assertEqual(
            [[0, 0], [0, 1], [1, 0], [1, 1]],
            self.solution.pacificAtlantic([
                [2, 1],
                [1, 2],
            ])
        )


if __name__ == '__main__':
    Test.execute()
