from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        total = 1
        zero_total = total
        zero_count = 0
        for num in nums:
            if num == 0:
                zero_count += 1
                if zero_count > 1:
                    return [0 for _ in range(0, len(nums))]
            else:
                zero_total *= num
            total *= num

        for num in nums:
            if num != 0:
                ans.append(int(total / num))
            else:
                ans.append(zero_total)

        return ans


if __name__ == '__main__':
    solution = Solution()
    print(solution.productExceptSelf([1, 2, 3, 4]))
    print(solution.productExceptSelf([-1, 1, 0, -3, 3]))
