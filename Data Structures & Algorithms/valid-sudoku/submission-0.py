class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[False] * 9 for _ in range(9)]
        col = [[False] * 9 for _ in range(9)]
        sq = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = ord(board[i][j]) - ord('1')
                    sqIndex = (i // 3) * 3 + (j // 3)

                    if row[i][num] or col[j][num] or sq[sqIndex][num]:
                        return False
                    
                    row[i][num] = True
                    col[j][num] = True
                    sq[sqIndex][num] = True
        return True