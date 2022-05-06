'''
Game Scene
Created buttons for my main menu
Buttons take to new scene
Image of monkey head in game
Handle method correctly takes user to the correct menu

'''






from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button


class GameScene(AbstractScene):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.button1 = Button(
            " Go Back  ",
            (50, 500),
            font=60,
            bg="navy")

        self.button2 = Button(
            " Easy ",
            (50, 150),
            font=50,
            bg="green")

        self.button3 = Button(
            " Easy ",
            (250, 150),
            font=50,
            bg="green")

        self.button4 = Button(
            " Medium ",
            (450, 150),
            font=50,
            bg="orange")

        self.button5 = Button(
            " Medium ",
            (50, 400),
            font=50,
            bg="orange")

        self.button6 = Button(
            " Hard ",
            (250, 400),
            font=50,
            bg="red")

        self.button7 = Button(
            " Hard ",
            (450, 400),
            font=50,
            bg="red")

    def render(self, screen):
        screen.fill((119, 221, 119))
        draw_text('GAME SCREEN', pygame.font.SysFont('Bauhaus 93', 65), (0, 0, 0), 50, 50, screen)
        self.button1.render(screen)
        self.button2.render(screen)
        self.button3.render(screen)
        self.button4.render(screen)
        self.button5.render(screen)
        self.button6.render(screen)
        self.button7.render(screen)
        draw_text(f'Banana: ${self.handler.banana}', pygame.font.SysFont('Bauhaus 93', 40), (255, 255, 0), 450, 25, screen)

    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("MAIN_SCENE")
        if self.button2.click(events):
            self.handler.go("EASY1_SCENE")
        if self.button3.click(events):
            self.handler.go("EASY2_SCENE")
        if self.button4.click(events):
            self.handler.go("MEDIUM1_SCENE")
        if self.button5.click(events):
            self.handler.go("MEDIUM2_SCENE")
        if self.button6.click(events):
            self.handler.go("HARD1_SCENE")
        if self.button7.click(events):
            self.handler.go("HARD2_SCENE")

    def update(self):
        pass
