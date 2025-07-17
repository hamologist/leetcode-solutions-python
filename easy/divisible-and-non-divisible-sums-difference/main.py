class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        answer = 0
        for num in range(1, n + 1):
            if num % m == 0:
                answer -= num
            else:
                answer += num

        return answer

print(Solution().differenceOfSums(10, 3))
