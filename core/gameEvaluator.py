from typing import Dict, Tuple


class GameEvaluator:

    isGameOver: bool = False


    def __init__(self):
        pass
        

    def checkIsGameOver(self,board) -> bool:
        self.board = board

        for player_color in [self.board.WHITE, self.board.BLACK]:
            allExistMoves = self.board.getAllExistMoves(player_color)
        
            if len(allExistMoves) == 0:
                self.isGameOver = True
        
        return self.isGameOver
    

    def getBlackWhiteScores(self,board) -> Tuple[int, int]:
        blackScore = 0
        whiteScore = 0
        board_list: Dict[Tuple[int, int], str] = board.board_list

        for pos, color in board_list.items():
            if color == board.BLACK:
                blackScore += 1
            elif color == board.WHITE:
                whiteScore += 1
        
        if blackScore==0 or whiteScore==0:
            self.isGameOver = True

        return blackScore, whiteScore
