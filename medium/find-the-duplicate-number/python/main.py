from collections import Counter
from typing import List

from _shared.python.test import BaseTest


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[0]

        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare

    def findDuplicateWithSet(self, nums: List[int]) -> int:
        lookup = set()
        for num in nums:
            if num in lookup:
                return num
            lookup.add(num)

    def findDuplicateWithCounter(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            2,
            self.solution.findDuplicate([1, 3, 4, 2, 2])
        )

    def test_two(self):
        self.assertEqual(
            3,
            self.solution.findDuplicate([3, 1, 3, 4, 2])
        )

    def test_three(self):
        self.assertEqual(
            1,
            self.solution.findDuplicate([1, 1])
        )

    def test_four(self):
        self.assertEqual(
            1,
            self.solution.findDuplicate([1, 1, 2])
        )


if __name__ == '__main__':
    Test.execute()
