from collections import Counter

from _shared.test import BaseTest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        lookup = set()
        for num in nums:
            if num in lookup:
                return True
            lookup.add(num)

        return False

    def containsDuplicateWithCounter(self, nums: list[int]) -> bool:
        return Counter(nums).most_common(1)[0][1] > 1


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            True,
            self.solution.containsDuplicate([1, 2, 3, 1])
        )

    def test_two(self):
        self.assertEqual(
            False,
            self.solution.containsDuplicate([1, 2, 3, 4])
        )

    def test_three(self):
        self.assertEqual(
            True,
            self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        )


if __name__ == '__main__':
    Test.execute()
