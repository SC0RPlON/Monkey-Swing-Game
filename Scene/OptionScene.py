from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button
import mixer


class OptionScene(AbstractScene):
    def __init__(self, swingsound, bananasound, scoresound):
        super().__init__()
        self.x = 0
        self.button1 = Button(
            " Go Back  ",
            (50, 500),
            font=60,
            bg="navy")
        self.button2 = Button(
            " Click here to mute all",
            (40, 150),
            font=27,
            bg="red")  # Creates a button called options with the attributes
        self.button3 = Button(
            " Click here to unmute all",
            (350, 150),
            font=27,
            bg="red")  # Creates a button called options with the attributes
        self.button4 = Button(
            " Click here to mute swing",
            (40, 250),
            font=27,
            bg="red")  # Creates a button called options with the attributes
        self.button5 = Button(
            " Click here to unmute swing",
            (350, 250),
            font=27,
            bg="red")
        self.button6 = Button(
            " Click here to mute banana",
            (40, 350),
            font=27,
            bg="red")
        self.button7 = Button(
            " Click here to unmute banana",
            (350, 350),
            font=27,
            bg="red")
        self.button8 = Button(
            " Click here to mute score",
            (40, 450),
            font=27,
            bg="red")
        self.button9 = Button(
            " Click here to unmute score",
            (350, 450),
            font=27,
            bg="red")
        # Creates a button called options with the attributes
        self.swingsound = swingsound
        self.bananasound = bananasound
        self.scoresound = scoresound

    def render(self, screen):
        screen.fill((119, 221, 119))
        draw_text('Options', pygame.font.SysFont('Bauhaus 93', 65), (0, 0, 0), 50, 50, screen)
        self.button1.render(screen)
        self.button2.render(screen)
        self.button3.render(screen)
        self.button4.render(screen)
        self.button5.render(screen)
        self.button6.render(screen)
        self.button7.render(screen)
        self.button8.render(screen)
        self.button9.render(screen)

    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("MAIN_SCENE")
        if self.button2.click(events):
            pygame.mixer.music.pause()
        if self.button3.click(events):
            pygame.mixer.music.unpause()
        if self.button4.click(events):
            self.handler.swingsound = True
        if self.button5.click(events):
            self.handler.swingsound = False
        if self.button6.click(events):
            self.handler.bananasound = True
        if self.button7.click(events):
            self.handler.bananasound = False
        if self.button8.click(events):
            self.handler.scoresound = True
        if self.button9.click(events):
            self.handler.scoresound = False

    def update(self):
        pass
