class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in range(len(board)):
            seen = set()
            for col in range(len(board)):
                if board[row][col] != ".":
                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col])
                else:
                    continue

        for row in range(len(board)):
            seen = set()
            for col in range(len(board)):
                if board[col][row] != ".":
                    if board[col][row] in seen:
                        return False
                    else:
                        seen.add(board[col][row])
                else:
                    continue 

        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3) * 3 + i
                    col = (square % 3) * 3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])
        return True