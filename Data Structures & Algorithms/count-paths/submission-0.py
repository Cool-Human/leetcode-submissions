class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1 for _ in range(n)] for _ in range(m)]

        def dp_top_down(r, c):
            nonlocal m
            nonlocal n
            nonlocal memo

            if r == m or c == n:
                return 0
            if memo[r][c] > 0:
                return memo[r][c]
            if r == m - 1 and c == n - 1:
                return 1
            
            memo[r][c] = dp_top_down(r + 1, c) + dp_top_down(r, c + 1)

            return memo[r][c]
        
        return dp_top_down(0, 0)