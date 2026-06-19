class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = [j for j in s1]
        m.sort()
        for i in range(len(s2) - len(m) + 1):
            n = [j for j in s2[i : i + len(m)]]
            n.sort()
            if n == m:
                return True
        return False