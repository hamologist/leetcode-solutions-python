from _shared.python.test import BaseTest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []

        nums.sort()
        for index in range(0, len(nums) - 1):
            if index == 0 or nums[index - 1] != nums[index]:
                low = index + 1
                high = len(nums) - 1
                target = -nums[index]
                while low < high:
                    if nums[low] + nums[high] == target:
                        res.append([nums[index], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] > target:
                        high -= 1
                    else:
                        low += 1

        return res


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            [[-1, -1, 2], [-1, 0, 1]],
            sorted(self.solution.threeSum([-1, 0, 1, 2, -1, -4]))
        )

    def test_two(self):
        self.assertEqual(
            [],
            self.solution.threeSum([])
        )

    def test_three(self):
        self.assertEqual(
            [],
            self.solution.threeSum([0])
        )


if __name__ == '__main__':
    Test.execute()
