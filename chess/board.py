class Board:
    def __init__(self):
        self.board = self.initialize_board()
        self.turn = "white"

    def initialize_board(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]

    def copy(self):
        new_board = Board()
        new_board.board = [row[:] for row in self.board]
        new_board.turn = self.turn
        return new_board

    def move_piece(self, from_row, from_col, to_row, to_col):
        self.board[to_row][to_col] = self.board[from_row][from_col]
        self.board[from_row][from_col] = " "
        self.turn = "black" if self.turn == "white" else "white"
