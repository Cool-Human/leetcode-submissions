class Solution:
    def uniquePaths(self, rows: int, cols: int) -> int:
        prevRow = [0 for _ in range(cols)]

        for r in range(rows - 1, -1, -1):
            curRow = [0 for _ in range(cols)]
            curRow[cols - 1] = 1 if r == rows - 1 else prevRow[cols - 1]
            for c in range(cols - 2, -1, -1):
                curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow
        
        return prevRow[0]