'''
Main Scene
Created buttons for my main menu
Buttons take to new scene
Image of monkey head in game

'''
from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button
from pygame import mixer

#calm background sound
pygame.mixer.init()
mixer.music.load('Assets/background.mp3')
mixer.music.play(-1) #plays music on loop


class MainScene(AbstractScene):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.button1 = Button(
            " Play   ",
            (50, 200),
            font=50,
            bg="navy") #Creates a button called play with the attributes

        self.button2 = Button(
            " Options   ",
            (50, 350),
            font=50,
            bg="red") #Creates a button called options with the attributes

        self.button3 = Button(
            " Characters   ",
            (50, 500),
            font=50,
            bg="green") #Creates a button called characters with the attributes

        self.head = pygame.image.load('Assets/MonkeyHead.png')
        #Creates a image with a monkey headD
        self.head = pygame.transform.scale(self.head, (320, 320))


    #Draws the screen and renders buttons and head
    def render(self, screen):
        screen.fill((119, 221, 119))
        draw_text('Swing Monkey Swing', pygame.font.SysFont('Bauhaus 93', 65), (0, 0, 0), 50, 50, screen)
        self.button1.render(screen)
        self.button2.render(screen)
        self.button3.render(screen)
        screen.blit(self.head, (350, 100))
        draw_text(f'Banana: ${self.handler.banana}', pygame.font.SysFont('Bauhaus 93', 40), (255, 255, 0), 450, 25, screen)
        draw_text(f'Total Score: ${self.handler.score}', pygame.font.SysFont('Bauhaus 93', 40), (25, 100, 100), 100, 25, screen)
        #draw_text(f'Bananas: ${self.handler.banana}', pygame.font.SysFont('Assets/Luducudu.ttf', 40), (255, 255, 0), 450, 30, screen)



#Checks for event changes and moves screen to option selected
    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("GAME_SCENE")
        if self.button2.click(events):
            self.handler.go("OPTION_SCENE")
        if self.button3.click(events):
            self.handler.go("CHARACTER_SCENE")

    def update(self):
        pass
