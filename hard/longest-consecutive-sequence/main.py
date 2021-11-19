from collections import deque
from _shared.test import BaseTest


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        memo = set(nums)
        longest_count = 0

        for num in nums:
            if num - 1 not in memo:
                check = num + 1
                current_count = 1

                while check in memo:
                    check += 1
                    current_count += 1

                longest_count = max(longest_count, current_count)

        return longest_count

    def longestConsecutiveUsingLookup(self, nums: list[int]) -> int:
        memo = {}
        longest_count = 0
        for num in nums:
            if num in memo:
                continue
            current_count = 1
            update_stack = deque()

            check = num - 1
            if check in memo:
                current_count += memo[check]
            while check in memo:
                update_stack.append(check)
                check -= 1

            check = num + 1
            if check in memo:
                current_count += memo[check]
            while check in memo:
                update_stack.append(check)
                check += 1

            for update in update_stack:
                memo[update] = current_count

            memo[num] = current_count
            longest_count = max(longest_count, current_count)

        return longest_count


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            4,
            self.solution.longestConsecutive([100, 4, 200, 1, 3, 2])
        )

    def test_two(self):
        self.assertEqual(
            9,
            self.solution.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        )

    def test_three(self):
        self.assertEqual(
            3,
            self.solution.longestConsecutive([1, 2, 0, 1])
        )


if __name__ == '__main__':
    Test.execute()
