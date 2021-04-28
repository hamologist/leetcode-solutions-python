from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = set()
        for num in nums:
            if num in ans:
                ans.remove(num)
            else:
                ans.add(num)

        return ans.pop()


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([2, 2, 1]))
    print(solution.singleNumber([4, 1, 2, 1, 2]))
    print(solution.singleNumber([1]))
