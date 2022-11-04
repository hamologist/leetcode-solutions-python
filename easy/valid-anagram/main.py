class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        left, right = [0] * 26, [0] * 26
        
        for char in s:
            left[ord(char) - 97] += 1
            
        for char in t:
            right[ord(char) - 97] += 1
        
        return tuple(left) == tuple(right)
