from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        res = []
        lookup = Counter(nums1)

        for num in nums2:
            if num in lookup:
                res.append(num)
                lookup[num] -= 1

                if lookup[num] == 0:
                    del (lookup[num])

        return res
