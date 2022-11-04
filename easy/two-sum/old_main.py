from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if target - num in lookup:
                return [i, lookup[target - num]]

            lookup[num] = i

    def twoSumOld(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for pos in range(0, len(nums)):
            num = nums[pos]
            update = num_map.get(num, [])
            update.append(pos)
            num_map[num] = update

        for num, positions in num_map.items():
            second = target - num
            if second in num_map:
                second_pos = num_map[second]
                if second == num and len(second_pos) < 2:
                    continue
                return [positions.pop(), second_pos.pop()]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum([2, 7, 11, 15], 9))
    print(solution.twoSum([3, 2, 4], 6))
    print(solution.twoSum([3, 3], 6))
