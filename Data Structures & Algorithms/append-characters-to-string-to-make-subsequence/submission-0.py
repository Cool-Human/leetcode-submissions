class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if s[j] == t[i]:
                i += 1
            j += 1
        return len(t) - i