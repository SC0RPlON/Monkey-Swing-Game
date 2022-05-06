'''
EasyScene1 Abstract class

methods:
    - render
        - This draws entities onto the screen
        - Draw Line from Monkey to top of screen to represent vines
        - Define Button
        - Draw and Update monkey groups
        - Check Score
        - Draw Score onto Screen
        - Detect Collisions
        - Create and Update new Trees
        - Draw and Scroll the ground
        - Check for game over and reset
    - reset
        - Resets game when character dies
    - handle
        - This will help with going back to main menu screen
        - Checks to see if game is correct for reset
    - update
        - This constantly checks for animations, gravity, character swinging, jumping and mouse clicks.

'''






from Scene.Scene import AbstractScene
from Misc import draw_text
import pygame
from Components.Button import Button
from Sprites.Monkey import Monkey
import random
from Sprites.Tree import Tree
from Components.ImageButton import ImageButton
from Sprites.Banana import Banana


class Medium2Scene(AbstractScene):
    def __init__(self, screen_height, screen_width) -> object:
        super().__init__()
        self.x = 0
        self.button1 = Button(
            " Go Back  ",
            (580, 410),
            font=40,
            bg="navy")

        self.screen_height = screen_height
        self.screen_width = screen_width

        # initalise monkey group
        self.monkey_group = pygame.sprite.Group()
        self.tree_group = pygame.sprite.Group()
        self.banana_group = pygame.sprite.Group()

        # initalise the monkey
        self.monkey = Monkey(100, int(screen_height / 2))  # pygame doesnt error float value so used int
        self.monkey_group.add(self.monkey)
        # initalise the trees
        # initialise the score
        self.score = 0

        # define game variables
        self.ground_scroll = 0
        self.scroll_speed = 4  # pixels each  iteration
        self.swinging = False
        self.game_over = False
        self.gap = 250  # pixels
        self.tfrequency = 500  # ms, how frequent i want trees
        self.last_tree = pygame.time.get_ticks() - self.tfrequency
        self.score = 0
        self.pass_tree = False

        # load in images
        self.ground = pygame.image.load('Assets/ground.png')
        self.bg = pygame.image.load('Assets/realbg.png')

        # initlaise end buttons
        self.butimg = pygame.image.load('Assets/restart.png')

        # first rate
        self.first = True

    def render(self, screen):
        screen.blit(self.bg, (0, 0))

        self.monkey.handler = self.handler

        # Draw Line from Monkey to top of screen to represent vines
        if self.game_over == False:
            pygame.draw.line(screen, (139, 69, 19),
                             (self.monkey_group.sprites()[0].rect.x + 20, self.monkey_group.sprites()[0].rect.y + 10),
                             (400, 0), 10)

        # define button
        self.button = ImageButton(self.screen_width // 2 - 50, self.screen_height // 2 - 100, self.butimg, screen)

        # Draw and Update monkey groups
        self.monkey_group.draw(screen)
        self.monkey_group.update()
        self.tree_group.draw(screen)
        self.banana_group.draw(screen)
        self.button1.render(screen)
        # Score Checker
        if len(self.tree_group) > 0:
            if self.monkey_group.sprites()[0].rect.left > self.tree_group.sprites()[0].rect.left \
                    and self.monkey_group.sprites()[0].rect.right < self.tree_group.sprites()[0].rect.right \
                    and self.pass_tree == False:
                self.pass_tree = True
            if self.pass_tree == True:
                if self.monkey_group.sprites()[0].rect.left > self.tree_group.sprites()[0].rect.right:
                    self.score += 1
                    self.pass_tree = False

        # Draws Score onto screen
        draw_text(str(self.score), pygame.font.SysFont('Bauhaus 93', 65), (0, 0, 0), int(self.screen_width / 2), 25,
                  screen)

        # detect collision between monkey and trees
        if pygame.sprite.groupcollide(self.monkey_group, self.tree_group, False,
                                      False) or self.monkey.rect.top < 0:  # loops for collision between two groups)
            self.game_over = True

        # detect collision between monkey and banana and increase score
        if pygame.sprite.groupcollide(self.monkey_group, self.banana_group, False, False):
            bana = self.banana_group.sprites().pop(0)
            bana.kill()
            self.handler.banana += 1
            print(self.handler.banana)

        # Checks to see if monkey touches bottom boundary
        if self.monkey.rect.bottom >= 449:
            self.game_over = True
            self.swinging = False

        if self.game_over == False and self.swinging == True:

            # create new trees
            current_time = pygame.time.get_ticks()
            if current_time - self.last_tree > self.tfrequency:
                tree_height = random.randint(-100, 100)
                btm_tree = Tree(self.screen_width, int(self.screen_height / 2) + tree_height, -1, 190)
                top_tree = Tree(self.screen_width, int(self.screen_height / 2) + tree_height, 1, 190)
                banana = Banana(int(self.screen_height / 2) + tree_height, self.screen_width, 3)
                self.tree_group.add(btm_tree)
                self.tree_group.add(top_tree)
                self.banana_group.add(banana)
                self.last_tree = current_time

            # draw and scroll the ground
            self.ground_scroll -= self.scroll_speed
            if abs(self.ground_scroll) > 35:
                self.ground_scroll = 0

            # update tree and banana gorups
            self.tree_group.update()
            self.banana_group.update()

        # check for game over and reset
        if self.game_over == True:
            if self.button.draw() == True:
                self.game_over = False
                self.tree_group.empty()
                self.monkey.rect.x = 100
                self.monkey.rect.y = int(self.screen_height / 2)
                score = 0
        screen.blit(self.ground, (self.ground_scroll, 449))

    # reset game function
    def reset_game(self):
        self.tree_group.empty()
        self.monkey.rect.x = 100
        self.monkey.rect.y = int(self.screen_height / 2)
        self.score = 0
        self.game_over = False

    # handle function
    def handle(self, events):
        if self.button1.click(events):
            self.handler.go("MAIN_SCENE")

        if pygame.mouse.get_pressed()[0] == 1 and self.swinging == False and self.game_over == False:
            self.swinging = True

        if self.button.click(events) and self.game_over == True:
            self.reset_game()

    def update(self):
        pass