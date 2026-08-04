class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        heatmap = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dp(row, col):
            nonlocal rows
            nonlocal cols
            nonlocal heatmap

            if row == rows or col == cols or obstacleGrid[row][col] == 1:
                return 0
            if heatmap[row][col] >= 0:
                return heatmap[row][col]
            if row == rows - 1 and col == cols - 1:
                return 1
            
            heatmap[row][col] = dp(row + 1, col) + dp(row, col + 1)
            return heatmap[row][col]
        
        return dp(0,0)