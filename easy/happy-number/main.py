class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()
        current = n
        while current != 1:
            if current in memo:
                return False
            build = 0
            for num in (int(num) for num in str(current)):
                build += num ** 2
            memo.add(current)
            current = build

        return True
