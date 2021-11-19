from _shared.test import BaseTest


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        column_title_length = len(columnTitle)
        for i in range(0, column_title_length):
            column_number += (26 ** (column_title_length - (i + 1))) * (ord(columnTitle[i]) - ord('A') + 1)

        return column_number


class Test(BaseTest[Solution]):
    _solution = Solution

    def test_one(self):
        self.assertEqual(
            1,
            self.solution.titleToNumber("A")
        )

    def test_two(self):
        self.assertEqual(
            28,
            self.solution.titleToNumber("AB")
        )

    def test_three(self):
        self.assertEqual(
            701,
            self.solution.titleToNumber("ZY")
        )

    def test_four(self):
        self.assertEqual(
            2147483647,
            self.solution.titleToNumber("FXSHRXW")
        )


if __name__ == '__main__':
    Test.execute()
