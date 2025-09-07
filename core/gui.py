# Example file showing a basic pygame "game loop"
import datetime
from typing import Counter

import pygame

from artificialInteligence import ArtificialIntelligence
from boardManagement import BoardManagement
from gameEvaluator import GameEvaluator


class Gui:
    board = None
    evaluator = GameEvaluator()
    ai = None
    
    RECTANGLE_SIZE = 70
    RECTANGLE_WIDTH = 500
    RECTANGLE_TOP_POSITION = 70
    RECTANGLE_LEFT_POSITION = 200
    screen = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)

    def __init__(self):
        self.rectangles = []
        self.ai = ArtificialIntelligence(evaluator=self.evaluator, depth=5)
        self.board = BoardManagement(self, self.evaluator, self.ai)

    def startPygameLoop(self):
        clock = pygame.time.Clock()
        running = True
        dt = 0

        # player position just for the grey circle
        player_pos = pygame.Vector2(
            self.screen.get_width() / 1.02, 
            self.screen.get_height() / 30
        )

        # init font ONCE
        pygame.font.init()
        my_font = pygame.font.SysFont("Comic Sans MS", 50)

        while running:
            # --- events ---
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if self.evaluator.checkIsGameOver(self.board):
                    black_score, white_score = self.evaluator.getBlackWhiteScores(self.board)
                    print(self.evaluator.getBlackWhiteScores(self.board))
                    text_to_display = "White Player Won."
                    if black_score > white_score:
                        text_to_display = "Black Player Won."

                    # render game-over text
                    text_surface = my_font.render(text_to_display, True, (255, 255, 255))
                    self.screen.blit(text_surface, (300, 10))
                    pygame.display.flip()

                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse clicked
                    for idx, r in enumerate(self.rectangles):
                        if r.collidepoint(event.pos):
                            self.board.onRectangleClickedAction(idx, self.board.WHITE)


            if self.evaluator.checkIsGameOver(self.board):
                continue
            # --- drawing ---
            self.screen.fill("black")
    
            pygame.draw.circle(self.screen, "grey", player_pos, 5)
            self.drawRectangles(self.board.board_list)
        
            # --- input keys ---
            keys = pygame.key.get_pressed()
            isMouseClicked = pygame.mouse.get_pressed()[0]
            if isMouseClicked:
                self.onMouseClickedCall()

            if keys[pygame.K_UP]:
                player_pos.y -= 300 * dt
            if keys[pygame.K_DOWN]:
                player_pos.y += 300 * dt
            if keys[pygame.K_LEFT]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_RIGHT]:
                player_pos.x += 300 * dt

            # --- flip / tick ---
            pygame.display.flip()
            dt = clock.tick(60) / 1000

        pygame.quit()

    def onMouseClickedCall(self):
        mousePos = pygame.mouse.get_pos()
        # print(datetime.datetime.now(), mousePos)

    def drawRectangles(self, board_list):
        self.rectangles = []  # reset list each frame

        # board starts centered on screen
        board_size = self.RECTANGLE_SIZE * 8
        offset_x = (self.screen.get_width() - board_size) // 2
        offset_y = (self.screen.get_height() - board_size) // 2

        for row in range(8):
            for col in range(8):
                left = offset_x + col * self.RECTANGLE_SIZE
                top = offset_y + row * self.RECTANGLE_SIZE
                rect = pygame.Rect(left, top, self.RECTANGLE_SIZE, self.RECTANGLE_SIZE)

                # draw green cell
                pygame.draw.rect(self.screen, "green", rect, 0)   # filled
                pygame.draw.rect(self.screen, "black", rect, 2)   # border

                # draw discs
                color = board_list[(row, col)]
                if color in ("white", "black"):  # valid disc
                    pygame.draw.circle(
                        self.screen,
                        color,
                        rect.center,
                        self.RECTANGLE_SIZE // 2 - 5
                    )

                self.rectangles.append(rect)


if __name__ == "__main__":
    g = Gui()
    g.startPygameLoop()
