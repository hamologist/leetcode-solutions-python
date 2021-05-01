from typing import Dict

from _shared.python.test import BaseTest

_ROMAN_LOOKUP: Dict[str, int] = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


class Solution:
    def romanToInt(self, s: str) -> int:
        prev = 0
        total = 0
        for rune in reversed(s):
            current = _ROMAN_LOOKUP[rune]

            if current >= prev:
                total += current
            else:
                total -= current
            prev = current

        return total


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            3,
            self.solution.romanToInt("III")
        )

    def test_two(self):
        self.assertEqual(
            4,
            self.solution.romanToInt("IV")
        )

    def test_three(self):
        self.assertEqual(
            9,
            self.solution.romanToInt("IX")
        )

    def test_four(self):
        self.assertEqual(
            58,
            self.solution.romanToInt("LVIII")
        )

    def test_five(self):
        self.assertEqual(
            1994,
            self.solution.romanToInt("MCMXCIV")
        )


if __name__ == '__main__':
    Test.execute()
