class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = dict()
        
        for i in range(0, len(nums)):
            if target - nums[i] in lookup:
                return [i, lookup[target - nums[i]]]
            
            lookup[nums[i]] = i
