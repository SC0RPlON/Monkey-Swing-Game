from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button

class GameScene(AbstractScene):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.button1 = Button(
            "Go Back",
            (100, 100),
            font=30,
            bg="navy")

    def render(self, screen):
        screen.fill((0, 255, 255))
        draw_text('GAME SCREEN', pygame.font.SysFont('Bauhaus 93', 70), (0, 0, 0), 10, 50, screen)
        self.button1.render(screen)

    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("MAIN_SCENE")

    def update(self):
        pass
