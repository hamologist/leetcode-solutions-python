from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        end = len(s)
        for i in range(0, int(end/2)):
            s[i], s[end - 1 - i] = s[end - 1 - i], s[i]


if __name__ == '__main__':
    solution = Solution()

    _input = list('hello')
    solution.reverseString(_input)
    print(_input)

    _input = list('Hannah')
    solution.reverseString(_input)
    print(_input)
