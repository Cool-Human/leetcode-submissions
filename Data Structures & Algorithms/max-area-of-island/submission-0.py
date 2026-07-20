class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        rows, cols = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if (min(r, c) < 0) or (r == rows) or (c == cols) or (grid[r][c] == 0) or ((r, c) in visit):
                return 0
            visit.add((r, c))
            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
        
        for i in range(rows):
            for j in range(cols):
                if (grid[i][j] == 1) and ((i, j) not in visit):
                    islandArea = dfs(i, j)
                    maxArea = max(islandArea, maxArea)
        
        return maxArea