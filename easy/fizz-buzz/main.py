from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        memo = []
        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                memo.append('FizzBuzz')
            elif num % 3 == 0:
                memo.append('Fizz')
            elif num % 5 == 0:
                memo.append('Buzz')
            else:
                memo.append(str(num))

        return memo


if __name__ == '__main__':
    solution = Solution()
    print(solution.fizzBuzz(3))
    print(solution.fizzBuzz(5))
    print(solution.fizzBuzz(15))
