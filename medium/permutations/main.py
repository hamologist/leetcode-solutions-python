from itertools import permutations
from typing import List


class Solution:
    def simple(self, nums: List[int]) -> List[List[int]]:
        return [list(perm) for perm in permutations(nums)]

    def permute(self, nums: List[int]) -> List[List[int]]:
        _answers = []
        _curr = []

        def _permute(_nums: List[int]):
            if len(_nums) == 0:
                _answers.append(_curr.copy())
                return

            for _pos in range(0, len(_nums)):
                _curr.append(_nums[_pos])
                _permute(_nums[:_pos] + _nums[_pos+1:])
                _curr.pop()

        _permute(nums)
        return _answers


if __name__ == '__main__':
    solution = Solution()
    print(solution.permute([1, 2, 3]))
    print(solution.permute([0, 1]))
    print(solution.permute([1]))
