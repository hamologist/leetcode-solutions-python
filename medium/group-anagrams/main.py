class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = dict()
        result = []
        
        for s in strs:
            key = [0] * 26
            for char in s:
                key[ord(char) - 97] += 1
            
            key = tuple(key)
            if key in lookup:
                result[lookup[key]].append(s)
            else:
                result.append([s])
                lookup[key] = len(result) - 1
        
        return result
