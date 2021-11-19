from _shared.test import BaseTest


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        count = 0
        memo = set()
        y_length = len(grid)
        x_length = len(grid[0])

        def dfs(_y: int, _x: int):
            if _x < 0 or _y < 0 or _x >= x_length or _y >= y_length or grid[_y][_x] == '0' or (_y, _x) in memo:
                return

            memo.add((_y, _x))
            dfs(_y - 1, _x)
            dfs(_y + 1, _x)
            dfs(_y, _x - 1)
            dfs(_y, _x + 1)

        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == '1' and (y, x) not in memo:
                    count += 1
                    dfs(y, x)

        return count


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            1,
            self.solution.numIslands([
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ])
        )

    def test_two(self):
        self.assertEqual(
            3,
            self.solution.numIslands([
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ])
        )


if __name__ == '__main__':
    Test.execute()
