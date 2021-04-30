from collections import deque
from typing import List

from _shared.python.test import BaseTest


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero_pointers = deque()
        for i in range(0, len(nums)):
            num = nums[i]
            if num == 0:
                zero_pointers.append(i)
            elif num != 0 and zero_pointers:
                zero_pos = zero_pointers.popleft()
                nums[i], nums[zero_pos] = nums[zero_pos], nums[i]
                zero_pointers.append(i)


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        _input = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(_input)
        self.assertEqual(
            [1, 3, 12, 0, 0],
            _input
        )

    def test_two(self):
        _input = [0]
        self.solution.moveZeroes(_input)
        self.assertEqual(
            [0],
            _input
        )


if __name__ == '__main__':
    Test.execute()
