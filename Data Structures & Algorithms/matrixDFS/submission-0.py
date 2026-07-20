class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visit = set()
        def dfs(grid, r, c, visit):
            ROW = len(grid)
            COL = len(grid[0])

            if (min(r, c) < 0) or (r == ROW) or (c == COL) or (grid[r][c] == 1) or ((r, c) in visit):
                return 0
            if (r == ROW - 1) and (c == COL - 1):
                return 1
            
            visit.add((r,c))

            count = 0

            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)

            visit.remove((r,c))
            return count
        return dfs(grid, 0, 0, visit)