class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        self.row = len(grid)
        self.col = len(grid[0])
        count = 0

        def dfs(grid, visit, r, c):
            if (min(r, c) < 0) or (r == self.row) or (c == self.col) or (grid[r][c] == "0") or ((r, c) in visit):
                return
            visit.add((r, c))
            dfs(grid, visit, r - 1, c)
            dfs(grid, visit, r + 1, c)
            dfs(grid, visit, r, c - 1)
            dfs(grid, visit, r, c + 1)
            

        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(grid, visit, i, j)
                    count += 1

        return count