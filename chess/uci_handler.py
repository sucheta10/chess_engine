import sys

from chess.board import Board


class UCIHandler:
    def __init__(self, search, move_generator):
        self.search = search
        self.move_generator = move_generator

    def handle_uci(self):
        sys.stdout.write("id name SimpleChessEngine\n")
        sys.stdout.write("id author YourName\n")
        sys.stdout.write("uciok\n")
        sys.stdout.flush()

    def handle_position(self, position):
        # Implement setting up the board from the position string
        pass

    def handle_go(self, command):
        board = Board()
        best_move = self.search.iterative_deepening(board, 3)  # Adjust depth as needed
        sys.stdout.write(f"bestmove {self.format_move(best_move)}\n")
        sys.stdout.flush()

    def format_move(self, move):
        from_row, from_col, to_row, to_col = move
        return f"{chr(from_col + ord('a'))}{8 - from_row}{chr(to_col + ord('a'))}{8 - to_row}"

    def handle_command(self, command):
        if command.startswith("uci"):
            self.handle_uci()
        elif command.startswith("position"):
            self.handle_position(command)
        elif command.startswith("go"):
            self.handle_go(command)
        else:
            sys.stderr.write(f"Unknown command: {command}\n")
            sys.stderr.flush()
