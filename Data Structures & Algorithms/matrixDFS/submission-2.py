class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        def dfs(grid, visit, r, c):
            row = len(grid)
            col = len(grid[0])

            if (min(r, c) < 0) or (r == row) or (c == col) or (grid[r][c] == 1) or ((r, c) in visit):
                return 0
            
            if (r == row - 1) and (c == col - 1):
                return 1
            
            visit.add((r, c))

            count = 0
            count += dfs(grid, visit, r + 1, c)
            count += dfs(grid, visit, r - 1, c)
            count += dfs(grid, visit, r, c + 1)
            count += dfs(grid, visit, r, c - 1)

            visit.remove((r, c))
            return count
        return dfs(grid, visit, 0, 0)