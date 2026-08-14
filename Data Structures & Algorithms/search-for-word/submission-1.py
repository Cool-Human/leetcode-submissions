class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        res = False

        def dfs(row, col, seen, idx):
            if idx == len(word):
                return True
            if not (0 <= row < rows and 0 <= col < cols) or (row, col) in seen or word[idx] != board[row][col]:
                return False
            
            seen.add((row, col))
            res = dfs(row + 1, col, seen, idx + 1) or dfs(row - 1, col, seen, idx + 1) or dfs(row, col + 1, seen, idx + 1) or dfs(row, col - 1, seen, idx + 1)
            seen.remove((row, col))
            return res
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    res = dfs(i, j, set(), 0)
                    if res:
                        return True
        return False