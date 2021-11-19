from typing import List

from _shared.test import BaseTest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit += max(prices[i] - prices[i - 1], 0)

        return max_profit


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            7,
            self.solution.maxProfit([7, 1, 5, 3, 6, 4])
        )

    def test_two(self):
        self.assertEqual(
            4,
            self.solution.maxProfit([1, 2, 3, 4, 5])
        )

    def test_three(self):
        self.assertEqual(
            0,
            self.solution.maxProfit([7, 6, 4, 3, 1])
        )


if __name__ == '__main__':
    Test.execute()
