class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                l = max(l, seen[s[i]] + 1)
            seen[s[i]] = i
            result = max(result, i - l + 1)

        return result
