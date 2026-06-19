class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = sorted(s1)
        for i in range(len(s2) - len(m) + 1):
            if sorted(s2[i : i + len(m)]) == m:
                return True
        return False