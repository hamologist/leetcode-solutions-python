class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        build = []
        check = {}
        for char in s:
            if char not in check:
                build.append(char)
                check[char] = len(build) - 1
            else:
                pos = check[char]
                build = build[pos+1:]
                build.append(char)
                check = {build[p]: p for p in range(0, len(build))}

            if len(build) > longest:
                longest = len(build)

        return longest


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))
    print(solution.lengthOfLongestSubstring("bbbbb"))
    print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("dvdf"))
    print(solution.lengthOfLongestSubstring("aabaab!bb"))
