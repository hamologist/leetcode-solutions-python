class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = [set() for _ in range(0, len(board))]
        cols = [set() for _ in range(0, len(board[0]))]
        squares = [
            [set() for _ in range(0, int(len(board[0]) / 3))]
            for _ in range(0, int(len(board) / 3))
        ]
        
        for r in range(0, len(board)):
            for c in range(0, len(board[r])):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])
                
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])
                
                if board[r][c] in squares[int(r / 3)][int(c / 3)]:
                    return False
                squares[int(r / 3)][int(c / 3)].add(board[r][c])

        return True

