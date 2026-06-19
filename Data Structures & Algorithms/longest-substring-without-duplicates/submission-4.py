class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        stack = []
        maxlength = 0

        i, j = 0, 0

        while j < len(s):
            if s[j] not in stack:
                stack.append(s[j])
                maxlength = max(maxlength, len(stack))
                j += 1
            elif s[j] == stack[0]:
                curr = stack.pop(0)
                stack.append(curr)
                maxlength = max(maxlength, len(stack))
                j += 1
            else:
                stack = []
                i = j
        
        return maxlength