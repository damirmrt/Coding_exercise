'''

'''


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        to_add = 1 if player == 1 else -1

        self.rows[row] += to_add
        self.cols[col] += to_add

        if row == col:
            self.diagonal += to_add

        if row + col == self.n - 1:
            self.anti_diagonal += to_add

        # Check win conditions
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
            return player

        return 0
    

from typing import List

def is_win_variant(board: List[List[int]], player: int, row: int, col: int) -> bool:
    board[row][col] = player
    n = len(board)

    rows = sum(1 for i in range(n) if board[row][i] == player)
    cols = sum(1 for i in range(n) if board[i][col] == player)
    diagonal = sum(1 for i in range(n) if board[i][i] == player)
    anti_diagonal = sum(1 for i in range(n) if board[i][n - 1 - i] == player)

    return rows == n or cols == n or diagonal == n or anti_diagonal == n