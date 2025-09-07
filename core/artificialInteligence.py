class ArtificialIntelligence:
    board = None

    def __init__(self, evaluator, depth=5):
        self.evaluator = evaluator
        self.depth = depth


    def miniMaxDecision(self, board, player_color):
        if self.board is None:
            self.board = board
        best_score = float('-inf')
        best_move = None

        # Get all possible moves for the player
        moves = self.board.getAllExistMoves(player_color)
        for move in moves:
            # Make a temporary board to simulate the move
            temp_board = self.simulateMove(self.board.board_list, move, player_color)
            score = self.minValue(temp_board, player_color, self.depth - 1)
            if score > best_score:
                best_score = score
                best_move = move

        print(f"AI bests:({best_move}->{best_score})")

        return best_move

    def maxValue(self, board_state, player_color, depth):
        if depth == 0 or self.evaluator.isGameOver:
            return self.evaluateBoard(board_state, player_color)

        value = float('-inf')
        moves = self.board.getAllExistMoves(player_color)
        for move in moves:
            temp_board = self.simulateMove(board_state, move, player_color)
            value = max(value, self.minValue(temp_board, player_color, depth - 1))
        return value

    def minValue(self, board_state, player_color, depth):
        if depth == 0 or self.evaluator.isGameOver:
            return self.evaluateBoard(board_state, player_color)

        opponent_color = self.board.BLACK if player_color == self.board.WHITE else self.board.WHITE
        value = float('inf')
        moves = self.board.getAllExistMoves(opponent_color)
        for move in moves:
            temp_board = self.simulateMove(board_state, move, opponent_color)
            value = min(value, self.maxValue(temp_board, player_color, depth - 1))
        return value

    def simulateMove(self, board_state, move, player_color):

        # Copy the board so we don't modify the original
        new_board = board_state.copy()

        # Place the new disc
        new_board[move] = player_color

        # fillTheRectangle
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1),  (1, 0), (1, 1)
        ]
        opponent = self.board.BLACK if player_color == self.board.WHITE else self.board.WHITE
        row, col = move

        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []
            while 0 <= r < 8 and 0 <= c < 8:
                if new_board[(r, c)] == opponent:
                    pieces_to_flip.append((r, c))
                    r += dr
                    c += dc
                elif new_board[(r, c)] == player_color:
                    for flip_r, flip_c in pieces_to_flip:
                        new_board[(flip_r, flip_c)] = player_color
                    break
                else:
                    break
        return new_board

    def evaluateBoard(self, board_state, player_color):
        opponent_color = self.board.BLACK if player_color == self.board.WHITE else self.board.WHITE
        player_score = sum(1 for c in board_state.values() if c == player_color)
        opponent_score = sum(1 for c in board_state.values() if c == opponent_color)
        return player_score - opponent_score
