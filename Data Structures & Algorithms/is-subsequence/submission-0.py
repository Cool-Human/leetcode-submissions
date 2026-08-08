class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        for i in range(len(s)):
            found = False
            while j < len(t):
                if t[j] == s[i]:
                    found = True
                    j += 1
                    break
                j += 1
            if not found:
                return False
        return True