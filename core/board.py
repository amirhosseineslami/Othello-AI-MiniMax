WHITE = "w"
BLACK = "B"
BLEAK = "-"


class Board:
    # This is our board data list
    board_list = {}
    
    def __init__(self):
        self.board_list = {}
        self.defineBoardList()
    
    def defineBoardList(self):

        for i in range(8):
            for j in range(8):
                self.board_list[(i,j)]=BLEAK

        self.board_list[(5,5)] = WHITE
        self.board_list[(4,4)] = WHITE
        self.board_list[(5,4)] = BLACK
        self.board_list[(4,5)] = BLACK

        print("Board is defined:")
        print(self.board_list)
            

if __name__ == "__main__":
    board = Board()
    board.defineBoardList()