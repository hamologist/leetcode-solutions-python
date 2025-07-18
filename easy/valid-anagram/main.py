class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0] * 26
        for char in s:
            check[ord(char) - 97] += 1

        for char in t:
            check[ord(char) - 97] -= 1

        for count in check:
            if count != 0:
                return False

        return True
