from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        pos = 1
        prev = nums[0]
        while pos < len(nums):
            if nums[pos] == prev:
                nums.pop(pos)
            else:
                prev = nums[pos]
                pos += 1

        return len(nums)


if __name__ == '__main__':
    solution = Solution()

    _input = [1, 1, 2]
    print(solution.removeDuplicates(_input))
    print(_input)

    _input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(solution.removeDuplicates(_input))
    print(_input)
