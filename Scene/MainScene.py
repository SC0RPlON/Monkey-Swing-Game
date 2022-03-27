'''
Main Scene

title

'''
from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button

class MainScene(AbstractScene):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.button1 = Button(
            "Play",
            (200, 200),
            font=30,
            bg="navy")

    def render(self, screen):
        screen.fill((255, 255, 255))
        draw_text('Swing Monkey Swing', pygame.font.SysFont('Bauhaus 93', 70), (0, 0, 0), 10, 50, screen)
        self.button1.render(screen)

    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("GAME_SCENE")

    def update(self):
        pass
