from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        memo = []

        def _inner(_remaining: List[int], _current: List[int]):
            memo.append(_current)

            for pos in range(0, len(_remaining)):
                _inner(_remaining[pos + 1:], _current + [_remaining[pos]])

        _inner(nums, [])
        return memo


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsets([1, 2, 3]))
    print(solution.subsets([0]))
