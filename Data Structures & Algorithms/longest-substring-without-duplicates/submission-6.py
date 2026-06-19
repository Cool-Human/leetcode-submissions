class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        stack = []
        maxLength = 0

        for r in range(len(s)):
            while s[r] in stack:
                stack.pop(0)
                l += 1
            stack.append(s[r])
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength