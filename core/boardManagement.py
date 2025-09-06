

from typing import Any


class BoardManagement:
    # This is our board data list
    board_list = {}
    WHITE = "white"
    BLACK = "black"
    isWhiteTurn = True
    BLEAK = ""

    def __init__(self):
        self.board_list = {}
        self.defineBoardList()
    
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
        y = rectangle_num//8
        x = rectangle_num%8
        print(x,y,allExistMoves)

        if (y,x) not in allExistMoves:
            return # Not in the feasible movements
        
        if not self.isWhiteTurn:
            return # Not White turn
        
        print("True")

        



            

if __name__ == "__main__":
    board = BoardManagement()
    board.defineBoardList()