from collections import Counter
from typing import Dict, List

from _shared.test import BaseTest


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lookup: Dict[str, int] = {}
        for letter in s:
            lookup[letter] = lookup.get(letter, 0) + 1
        for letter in t:
            count = lookup.get(letter, 0) - 1
            if count < 0:
                return False
            lookup[letter] = count

        return True

    def isAnagramWithList(self, s: str, t: str) -> bool:
        s_lookup: List[int] = [0] * 26
        t_lookup: List[int] = [0] * 26
        for letter in s:
            s_lookup[ord(letter) - ord('a')] += 1
        for letter in t:
            t_lookup[ord(letter) - ord('a')] += 1

        return s_lookup == t_lookup

    def isAnagramWithCounter(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertTrue(
            self.solution.isAnagram("anagram", "nagaram")
        )

    def test_two(self):
        self.assertFalse(
            self.solution.isAnagram("rat", "car")
        )


if __name__ == '__main__':
    Test.execute()
