from math import inf
from _shared.python.test import BaseTest


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_max = -inf
        current = current_max

        for num in nums:
            if (current < 0 and num < 0) or current < 0 <= num:
                current = 0
            current += num

            current_max = max(current_max, current)

        return current_max


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            6,
            self.solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        )

    def test_two(self):
        self.assertEqual(
            1,
            self.solution.maxSubArray([1])
        )

    def test_three(self):
        self.assertEqual(
            23,
            self.solution.maxSubArray([5, 4, -1, 7, 8])
        )


if __name__ == '__main__':
    Test.execute()
