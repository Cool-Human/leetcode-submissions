class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        points = []

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    points.append([i,j])
        
        while points:
            i, j = points.pop()
            for x in range(rows):
                matrix[x][j] = 0
            for y in range(cols):
                matrix[i][y] = 0
        
        return