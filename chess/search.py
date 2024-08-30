class Search:
    def __init__(self, move_generator, evaluator):
        self.move_generator = move_generator
        self.evaluator = evaluator

    def iterative_deepening(self, board, max_depth):
        best_move = None
        best_value = -float("inf")
        for depth in range(1, max_depth + 1):
            move, value = self.alpha_beta(board, depth, -float("inf"), float("inf"), True)
            if value > best_value:
                best_value = value
                best_move = move
        return best_move

    def alpha_beta(self, board, depth, alpha, beta, maximizing_player):
        if depth == 0:
            return None, self.evaluator.evaluate(board)

        moves = self.move_generator.generate_all_moves(board, board.turn)
        if maximizing_player:
            max_eval = -float("inf")
            best_move = None
            for move in moves:
                new_board = board.copy()
                self.make_move(new_board, move)
                _, eval = self.alpha_beta(new_board, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return best_move, max_eval
        else:
            min_eval = float("inf")
            best_move = None
            for move in moves:
                new_board = board.copy()
                self.make_move(new_board, move)
                _, eval = self.alpha_beta(new_board, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return best_move, min_eval

    def make_move(self, board, move):
        from_row, from_col, to_row, to_col = move
        board.move_piece(from_row, from_col, to_row, to_col)
