import heapq

from _shared.python.test import BaseTest


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    def findKthLargestWithSort(self, nums: list[int], k: int) -> int:
        return sorted(nums)[-k]


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            5,
            self.solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
        )

    def test_two(self):
        self.assertEqual(
            4,
            self.solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        )


if __name__ == '__main__':
    Test.execute()
