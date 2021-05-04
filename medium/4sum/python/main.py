class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = []
        nums.sort()

        def two_sum(_left: int, _target: int) -> list[(int, int)]:
            _res = []
            _right = len(nums) - 1
            while _left < _right:
                if nums[_left] + nums[_right] == _target:
                    _res.extend([(nums[_left], nums[_right])])
                    while _left < _right and nums[_left + 1] == nums[_left]:
                        _left += 1
                    while _left < _right and nums[_right - 1] == nums[_right]:
                        _right -= 1
                    _left += 1
                    _right -= 1
                elif nums[_left] + nums[_right] > _target:
                    _right -= 1
                elif nums[_left] + nums[_right] < _target:
                    _left += 1

            return _res

        prev_i = None
        for i in range(0, len(nums) - 3):
            if prev_i == nums[i]:
                continue
            prev_i = nums[i]
            prev_j = None
            for j in range(i + 1, len(nums) - 2):
                if prev_j == nums[j]:
                    continue
                prev_j = nums[j]
                sums = two_sum(j + 1, target - (nums[i] + nums[j]))
                if sums:
                    res.extend([[nums[i], nums[j], cd[0], cd[1]] for cd in sums])

        return res