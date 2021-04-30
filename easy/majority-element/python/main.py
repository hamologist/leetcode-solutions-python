from collections import Counter
from typing import Dict, List

from _shared.python.test import BaseTest


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        vote = 0
        current = None
        for num in nums:
            if vote == 0:
                current = num
            vote += 1 if current == num else -1

        return current

    def majorityElementWithLookup(self, nums: List[int]) -> int:
        counter: Dict[int, int] = {}
        target = int(len(nums) / 2)
        for num in nums:
            count = counter.get(num, 0) + 1
            counter[num] = count
            if count > target:
                return num

    def majorityElementWithCounter(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(self.solution.majorityElement([3, 2, 3]), 3)

    def test_two(self):
        self.assertEqual(self.solution.majorityElement([2, 2, 1, 1, 1, 2, 2]), 2)


if __name__ == '__main__':
    Test.execute()
