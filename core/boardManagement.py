import traceback
from turtle import tracer


class BoardManagement:
    # This is our board data list
    board_list = {}
    WHITE = "white"
    BLACK = "black"
    isWhiteTurn = True
    BLEAK = ""
    AI_PLAYER_COLOR = BLACK

    def __init__(self,gui,evaluator,ai):
        self.board_list = {}
        self.defineBoardList()
        self.gui = gui
        self.evaluator = evaluator
        self.ai = ai
    
    def defineBoardList(self):

        for i in range(8):
            for j in range(8):
                self.board_list[(i,j)]=self.BLEAK

        self.board_list[(4,4)] = self.WHITE
        self.board_list[(3,3)] = self.WHITE
        self.board_list[(4,3)] = self.BLACK
        self.board_list[(3,4)] = self.BLACK

        print("Board is defined:")
        print(self.board_list)


    def getAllExistMoves(self, player_color):
        """Return all valid moves for the given player."""
        opponent = self.BLACK if player_color == self.WHITE else self.WHITE
        directions = [
            (-1, -1), (-1, 0), (-1, 1),  # Up-left, up, up-right
            (0, -1),          (0, 1),    # Left, right
            (1, -1),  (1, 0), (1, 1)     # Down-left, down, down-right
        ]

        valid_moves = set()

        for row in range(8):
            for col in range(8):
                if self.board_list[(row, col)] != self.BLEAK:
                    continue  # skip non-empty squares

                # Check all 8 directions
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    found_opponent = False

                    while 0 <= r < 8 and 0 <= c < 8:
                        piece = self.board_list[(r, c)]
                        if piece == opponent:
                            found_opponent = True
                            r += dr
                            c += dc
                        elif piece == player_color and found_opponent:
                            valid_moves.add((row, col))
                            break
                        else:
                            break

        return valid_moves
    
    def onRectangleClickedAction(self,rectangle_num, player_color):
        """Act if the action is feasible."""
        allExistMoves = self.getAllExistMoves(player_color)
        
        if len(allExistMoves) == 0:
            self.evaluator.isGameOver = True
            return

        y = rectangle_num//8
        x = rectangle_num%8
        #print(x,y,allExistMoves)

        if (y,x) not in allExistMoves:
            return # Not in the feasible movements
        
        if not self.isWhiteTurn:
            return # Not White turn
        
        print("True")

        # Let's fill the rectangles
        self.fillTheRectangle((y,x),player_color)
        self.isWhiteTurn = False

        # It's Ai's turn
        ai_best_move = self.ai.miniMaxDecision(self,self.AI_PLAYER_COLOR)
        self.fillTheRectangle(ai_best_move,self.AI_PLAYER_COLOR)
        self.isWhiteTurn = True
        


    def fillTheRectangle(self, rectPosition, player_color):
        self.board_list[rectPosition] = player_color

        try:
            opponent = self.BLACK if player_color == self.WHITE else self.WHITE
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)
            ]
            row, col = rectPosition
        except Exception as e:
            traceback.print_exc()
        

        # Check all 8 directions
        for dr, dc in directions:
            r, c = row + dr, col + dc
            pieces_to_flip = []

            # Scan in this direction
            while 0 <= r < 8 and 0 <= c < 8:
                current_piece = self.board_list[(r, c)]
                if current_piece == opponent:
                    pieces_to_flip.append((r, c))
                    r += dr
                    c += dc
                elif current_piece == player_color:
                    # Found bounding piece → flip all in between
                    for flip_r, flip_c in pieces_to_flip:
                        self.board_list[(flip_r, flip_c)] = player_color
                    break
                else:
                    # Empty or BLEAK cannot flip in this direction
                    break

            

if __name__ == "__main__":
    board = BoardManagement()
    board.defineBoardList()