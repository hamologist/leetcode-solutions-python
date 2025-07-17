class Solution:
    def getSneakyNumbers(self, nums: list[int]) -> list[int]:
        memo = set()

        ans = []
        for num in nums:
            if num in memo:
                ans.append(num)
                if len(ans) == 2:
                    break
            memo.add(num)

        return ans

