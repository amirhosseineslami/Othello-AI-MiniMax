# Example file showing a basic pygame "game loop"
import datetime
from os import name

import pygame

from core.board import Board


class Gui:
    board = Board()

    def startPygameLoop(self):
        # pygame setup
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        clock = pygame.time.Clock()
        running = True
        dt = 0

        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
        pygame.event.get()
        pygame.event.wait()

        while running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # fill the screen with a color to wipe away anything from last frame
            screen.fill("purple")

            pygame.draw.circle(screen, "red", player_pos, 40)

            keys = pygame.key.get_pressed()
            
            isMouseClicked = pygame.mouse.get_pressed()[0]
            if(isMouseClicked):
                self.onMouseClickedCall()



            if keys[pygame.K_w]:
                player_pos.y -= 300 * dt
            if keys[pygame.K_s]:
                player_pos.y += 300 * dt
            if keys[pygame.K_a]:
                player_pos.x -= 300 * dt
            if keys[pygame.K_d]:
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
        print(datetime.datetime.now(),mousePos)


if __name__ == "__main__":
    g = Gui()
    g.startPygameLoop()
