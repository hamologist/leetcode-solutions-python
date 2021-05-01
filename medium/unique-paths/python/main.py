from _shared.python.test import BaseTest


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[0 for _ in range(n)] for _ in range(m)]
        for y in range(m):
            for x in range(n):
                if y == 0 or x == 0:
                    matrix[y][x] = 1
                else:
                    matrix[y][x] = matrix[y - 1][x] + matrix[y][x - 1]

        return matrix[-1][-1]

    def uniquePathsWithRecursion(self, m: int, n: int) -> int:
        memo: dict[(int, int), int] = {}

        def _inner(y: int, x: int) -> int:
            if y == m and x == n:
                return 1
            if y > m or x > n:
                return 0

            if (cord := (y + 1, x)) in memo:
                count = memo[cord]
            else:
                count = _inner(y + 1, x)

            if (cord := (y, x + 1)) in memo:
                count += memo[cord]
            else:
                count += _inner(y, x + 1)

            memo[(y, x)] = count
            return count

        return _inner(1, 1)


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            28,
            self.solution.uniquePaths(3, 7)
        )

    def test_two(self):
        self.assertEqual(
            3,
            self.solution.uniquePaths(3, 2)
        )

    def test_three(self):
        self.assertEqual(
            28,
            self.solution.uniquePaths(7, 3)
        )

    def test_four(self):
        self.assertEqual(
            6,
            self.solution.uniquePaths(3, 3)
        )


if __name__ == '__main__':
    Test.execute()
