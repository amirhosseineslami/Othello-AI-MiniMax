# Example file showing a basic pygame "game loop"
import datetime
from cmath import rect
from ctypes.wintypes import RECT
from os import name
from turtle import color

import pygame
from boardManagement import BoardManagement


class Gui:
    board = BoardManagement()
    
    RECTANGLE_SIZE = 70
    RECTANGLE_WIDTH = 500
    RECTANGLE_TOP_POSITION = 70
    RECTANGLE_LEFT_POSITION = 200
    screen = pygame.display.set_mode((1080, 720), pygame.RESIZABLE)


    def __init__(self):
        self.rectangles = []

    def startPygameLoop(self):
        clock = pygame.time.Clock()
        running = True
        dt = 0

        player_pos = pygame.Vector2(self.screen.get_width() / 1.02, self.screen.get_height() / 30)
        pygame.event.get()
        pygame.event.wait()

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:  # mouse clicked

                    for idx, r in enumerate(self.rectangles):

                        if r.collidepoint(event.pos):      # check click inside rect
                            print(f"Rectangle {idx} clicked at {event.pos}")
                            # User clicked a rectangle
                            self.board.onRectangleClickedAction(idx,self.board.WHITE)
                
                




            # fill the screen with a color to wipe away anything from last frame
            self.screen.fill("black")

            pygame.draw.circle(self.screen, "grey", player_pos, 5)
            self.drawRectangles(self.board.board_list)


            keys = pygame.key.get_pressed()
            
            isMouseClicked = pygame.mouse.get_pressed()[0]
            if(isMouseClicked):
                self.onMouseClickedCall()




            if keys[pygame.K_UP]:
                player_pos.y -= 300 * dt
            if keys[pygame.K_DOWN]:
                player_pos.y += 300 * dt
            if keys[pygame.K_LEFT]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_RIGHT]:
                player_pos.x += 300 * dt

            # flip() the display to put your work on screen
            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

        pygame.quit()

    def onMouseClickedCall(self):
        mousePos = pygame.mouse.get_pos()
        #print(datetime.datetime.now(),mousePos)

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

    # def drawRectangles(self,board_list):
    #     self.rectangles = []  # reset list each frame
    #     accumulate_num = self.screen.get_height() / 15

    #     for i in range(8):
    #         accumulate_num = self.screen.get_height() / 15
    #         for j in range(8):
    #             left = self.RECTANGLE_LEFT_POSITION * (i) / 2.5 + self.screen.get_width() / 4.5
    #             top = self.RECTANGLE_TOP_POSITION * (j) + accumulate_num
    #             rect = pygame.Rect(
    #                 left,
    #                 top,
    #                 self.RECTANGLE_SIZE,
    #                 self.RECTANGLE_SIZE,
    #             )
    #             pygame.draw.rect(self.screen, "green", rect, self.RECTANGLE_WIDTH)

    #             # Draw circles in it
    #             color = board_list[(j,i)]
    #             if len(color) > 1:
    #                 pygame.draw.circle(surface=self.screen, color= color, center=pygame.Vector2(left + self.RECTANGLE_SIZE/2, top + self.RECTANGLE_SIZE/2),radius=self.RECTANGLE_WIDTH)
                
    #             self.rectangles.append(rect)  # store for click detection
    #             accumulate_num += 10
        


if __name__ == "__main__":
    g = Gui()
    g.startPygameLoop()
