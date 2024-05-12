from scripts.constants import *
from scripts.input import Input
import pygame, sys


class Game:
    def __init__(self) -> None:
        self.is_running = False
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        self.input = Input(self)
        self.clock = pygame.time.Clock()

        self.set_title()

    def set_title(self):
        pygame.display.set_caption(GAME_TITLE)

    def render_fps(self):
        fps = GAME_FONT.render(f"FPS: {self.clock.get_fps():.2f}", True, Color("White"))

        self.screen.blit(fps, (5, 5))

    def update(self, dt):
        pass

    def render(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.render_fps()

        pygame.display.update()

    def quit(self):
        self.is_running = False

        pygame.quit()
        sys.exit()

    def run(self):
        self.is_running = True

        while self.is_running:
            dt = self.clock.tick(FPS) / 1000.0

            self.input.process()

            self.update(dt)
            self.render()

            self.input.flush()


Game().run()
