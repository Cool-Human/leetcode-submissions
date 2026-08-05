from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = 0
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        fresh_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append([r,c])
                elif grid[r][c] == 1:
                    fresh_count += 1
        
        if fresh_count == 0: return 0

        while queue and fresh_count > 0:
            time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in ([1,0], [-1,0], [0,1], [0,-1]):
                    nr, nc = r + dr, c + dc
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh_count -= 1
                        queue.append([nr, nc])
        
        if fresh_count != 0: return -1
        
        return time