class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1

        while left <= right:
            middle = left + (right - left) // 2
            
            row = middle // len(matrix[0])
            col = middle % len(matrix[0])

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False