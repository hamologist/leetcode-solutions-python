import heapq
from math import inf
from bisect import bisect
from itertools import chain

from _shared.test import BaseTest


class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        def analyze(_mid: int) -> (int, int):
            _count = 0
            _num = -inf
            for row in matrix:
                index = bisect(row, _mid)

                if index == 0:
                    break

                _count += index
                if index:
                    _num = max(_num, row[index - 1])

            return _count, _num

        left = matrix[0][0]
        right = matrix[-1][-1]
        ans = matrix[0][0]
        while left <= right:
            mid = (left + right) // 2
            count, num = analyze(mid)
            if count >= k:
                ans = num
                right = mid - 1
            else:
                left = mid + 1

        return ans

    def kthSmallestWithSort(self, matrix: list[list[int]], k: int) -> int:
        return sorted(chain.from_iterable(matrix))[k - 1]

    def kthSmallestWithHeap(self, matrix: list[list[int]], k: int) -> int:
        heap = [(matrix[0][0], 0, 0)]
        memo = {(0, 0)}
        count = 0
        current = 0
        n = len(matrix)
        while count < k:
            current, y, x = heapq.heappop(heap)
            if (y, x + 1) not in memo and x + 1 < n:
                heapq.heappush(heap, (matrix[y][x + 1], y, x + 1))
                memo.add((y, x + 1))

            if (y + 1, x) not in memo and y + 1 < n:
                heapq.heappush(heap, (matrix[y + 1][x], y + 1, x))
                memo.add((y + 1, x))

            count += 1

        return current


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            13,
            self.solution.kthSmallest([
                [1, 5, 9],
                [10, 11, 13],
                [12, 13, 15],
            ], 8)
        )

    def test_two(self):
        self.assertEqual(
            -5,
            self.solution.kthSmallest([[-5]], 1)
        )

    def test_three(self):
        self.assertEqual(
            5,
            self.solution.kthSmallest([
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30]
            ], 5)
        )

    def test_four(self):
        self.assertEqual(
            11,
            self.solution.kthSmallest([
                [1, 3, 5],
                [6, 7, 12],
                [11, 14, 14]
            ], 6)
        )


if __name__ == '__main__':
    Test.execute()
