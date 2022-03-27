'''
Main Scene

title

'''
from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame


class MainScene(AbstractScene):
    def __init__(self):
        super().__init__()
        self.x = 0

    def render(self, screen):
        screen.fill((255, 255, 255))
        draw_text('Swing Monkey Swing', pygame.font.SysFont('Bauhaus 93', 70), (0, 0, 0), 10, 50, screen)


    def handle(self, events):
        pass

    def update(self):
        pass
