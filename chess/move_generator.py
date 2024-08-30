class MoveGenerator:
    def generate_all_moves(self, board, color):
        moves = []
        for y in range(8):
            for x in range(8):
                if (color == "white" and board.board[y][x].isupper()) or (color == "black" and board.board[y][x].islower()):
                    piece_moves = self.get_piece_moves(board, y, x)
                    moves.extend(piece_moves)
        return moves

    def get_piece_moves(self, board, y, x):
        piece = board.board[y][x].lower()
        moves = []
        if piece == "p":
            moves.extend(self.get_pawn_moves(board, y, x))
        elif piece == "r":
            moves.extend(self.get_rook_moves(board, y, x))
        # Add more pieces here
        return moves

    def get_pawn_moves(self, board, y, x):
        moves = []
        direction = -1 if board.turn == "white" else 1
        if 0 <= y + direction < 8:
            if board.board[y + direction][x] == " ":
                moves.append((y, x, y + direction, x))
        return moves

    def get_rook_moves(self, board, y, x):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            while 0 <= ny < 8 and 0 <= nx < 8 and board.board[ny][nx] == " ":
                moves.append((y, x, ny, nx))
                ny += dy
                nx += dx
        return moves
