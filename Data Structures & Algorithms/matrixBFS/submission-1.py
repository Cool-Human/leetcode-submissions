class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        visit = set()

        if grid[0][0] == 1:
            return -1
        
        if rows == 1 and cols == 1:
            return 0

        queue.append((0,0, 0))
        visit.add((0,0))

        while queue:
            r, c, length = queue.popleft()

            neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
            for dr, dc in neighbours:
                row = r + dr
                col = c + dc

                if min(row, col) < 0 or row == rows or col == cols or grid[row][col] == 1 or (row,col) in visit:
                    continue
                
                if row == rows - 1 and col == cols - 1:
                    return length + 1
                
                visit.add((row,col))
                queue.append((row,col, length + 1))
        return -1