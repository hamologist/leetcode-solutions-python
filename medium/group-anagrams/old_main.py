from typing import Dict, List, Tuple

from _shared.test import BaseTest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup: Dict[str, List[str]] = {}
        for word in strs:
            key = str(sorted(word))
            if key in lookup:
                lookup.get(key).append(word)
            else:
                lookup[key] = [word]

        return list(lookup.values())

    def groupAnagramsByLookup(self, strs: List[str]) -> List[List[str]]:
        lookup: Dict[Tuple, List[str]] = {}
        for word in strs:
            letter_lookup = [0] * 26
            for letter in word:
                letter_lookup[ord(letter) - 97] += 1

            key = tuple(letter_lookup)
            if key in lookup:
                lookup.get(key).append(word)
            else:
                lookup[key] = [word]

        return list(lookup.values())


class Test(BaseTest[Solution]):
    _solution = Solution

    @staticmethod
    def sort_elements(elements: List[List]) -> List[List]:
        return sorted([sorted(element) for element in elements])

    def test_one(self):
        self.assertCountEqual(
            [['bat'], ['nat', 'tan'], ['ate', 'eat', 'tea']],
            self.sort_elements(self.solution.groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
        )

    def test_two(self):
        self.assertCountEqual(
            [['']],
            self.solution.groupAnagrams([''])
        )

    def test_three(self):
        self.assertCountEqual(
            [['a']],
            self.solution.groupAnagrams(['a'])
        )


if __name__ == '__main__':
    Test.execute()
