class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1
        
        for num, count in lookup.items():
            bucket[count].append(num)
        
        result = []
        for orderedNums in bucket[::-1]:
            for num in orderedNums:
                result.append(num)
                k -= 1
                
                if k == 0:
                    break
            if k == 0:
                break
        
        return result
