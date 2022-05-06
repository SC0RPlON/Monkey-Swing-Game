from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button


class CharacterScene(AbstractScene):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.button1 = Button(
            " Go Back  ",
            (50, 500),
            font=60,
            bg="navy")
        self.button2 = Button(
            " 200 Bananas  ",
            (50, 150),
            font=40,
            bg="black")
        self.button3 = Button(
            " 400 Bananas  ",
            (400, 150),
            font=40,
            bg="black")
        self.head = pygame.image.load('Assets/MonkeyHead2.png')
        # Creates a image with a monkey headD
        self.head = pygame.transform.scale(self.head, (320, 320))
        self.head2 = pygame.image.load('Assets/MonkeyHead3.png')
        # Creates a image with a monkey headD
        self.head2 = pygame.transform.scale(self.head2, (320, 320))

    def render(self, screen):
        screen.fill((119, 221, 119))
        draw_text('When you have enough bananas, change your character', pygame.font.SysFont('Bauhaus 93', 20), (0, 0, 0), 50, 50, screen)
        self.button1.render(screen)
        self.button2.render(screen)
        self.button3.render(screen)
        screen.blit(self.head, (50, 200))
        screen.blit(self.head2, (350, 200))

    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("MAIN_SCENE")
        if self.button2.click(events) and self.handler.banana == 0:
            self.handler.monkeytype = 2
        if self.button3.click(events) and self.handler.banana == 0:
            self.handler.monkeytype = 3



    def update(self):
        pass
