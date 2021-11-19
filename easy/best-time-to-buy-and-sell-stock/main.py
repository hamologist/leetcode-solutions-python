import math


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        current_min = math.inf
        current_max_profit = 0
        for price in prices:
            current_max_profit = max(current_max_profit, price - current_min)
            current_min = min(current_min, price)

        return current_max_profit
