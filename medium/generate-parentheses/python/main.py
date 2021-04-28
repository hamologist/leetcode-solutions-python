from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        memo = []

        def _inner(_left: int, _right: int, _current: str):
            if _right == n:
                memo.append(_current)

            if _left < n:
                _inner(_left + 1, _right, _current + "(")

            if _right < n and _left > _right:
                _inner(_left, _right + 1, _current + ")")

        _inner(0, 0, "")
        return memo


if __name__ == '__main__':
    solution = Solution()
    print(solution.generateParenthesis(3))
    print(solution.generateParenthesis(1))
