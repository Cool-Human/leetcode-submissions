class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        a = len(text1)
        b = len(text2)

        cache = {}
        def dp(i, j):
            if i == a or j == b:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                cache[(i, j)] = 1 + dp(i + 1, j + 1)
            else:
                cache[(i, j)] = max(dp(i + 1, j), dp(i, j + 1))
            
            return cache[(i, j)]

        return dp(0,0)