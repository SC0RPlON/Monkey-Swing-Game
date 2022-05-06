'''
SceneHandler Abstract class

methods:
    - go
        - This goes to a Scene

'''
# import the scenes from scene file
from Scene.GameScene import GameScene
from Scene.MainScene import MainScene
from Scene.OptionScene import OptionScene
from Scene.CharacterScene import CharacterScene
from Scene.Easy1Scene import Easy1Scene
from Scene.Easy2Scene import Easy2Scene
from Scene.Medium1Scene import Medium1Scene
from Scene.Medium2Scene import Medium2Scene
from Scene.Hard1Scene import Hard1Scene
from Scene.Hard2Scene import Hard2Scene
import pygame


# scene handler class
class SceneHandler(object):
    def __init__(self, screen_heights, screen_width):
        self.swingsound = False
        self.bananasound = False
        self.scoresound = False
        self.monkeys_dict = {1: "Assets/m1.png", 2: "Assets/m2.png", 3: "Assets/m3.png"}
        self.go("MAIN_SCENE")  # this starts off at main scene
        self.screen_height = screen_heights # initialise screen height
        self.screen_width = screen_width    # initialise screen width
        self.banana = 0 # set banana coins to 0
        self.score = 0 # set score to 0
        self.monkeytype = 1

# function of where the scene will change to if certain buttons are pressed
    def go(self, scene):
        if scene == "GAME_SCENE":       # if this is pressed, set scene to Game scene
            self.scene = GameScene()
        if scene == "MAIN_SCENE":       # if this is pressed, set scene to Main scene
            self.scene = MainScene()
        if scene == "OPTION_SCENE":     # if this is pressed, set scene to Option scene
            self.scene = OptionScene(swingsound=False, bananasound=False, scoresound=False)
        if scene == "CHARACTER_SCENE":  # if this is pressed, set scene to Character scene
            self.scene = CharacterScene()
        if scene == "EASY1_SCENE":
            self.scene = Easy1Scene(self.screen_height, self.screen_width, self.monkeys_dict[self.monkeytype])
        self.scene.handler = self
        if scene == "EASY2_SCENE":
            self.scene = Easy2Scene(self.screen_height, self.screen_width, self.monkeys_dict[self.monkeytype])
        self.scene.handler = self
        if scene == "MEDIUM1_SCENE":
            self.scene = Medium1Scene(self.screen_height, self.screen_width, self.monkeys_dict[self.monkeytype])
        self.scene.handler = self
        if scene == "MEDIUM2_SCENE":
            self.scene = Medium2Scene(self.screen_height, self.screen_width, self.monkeys_dict[self.monkeytype])
        self.scene.handler = self
        if scene == "HARD1_SCENE":
            self.scene = Hard1Scene(self.screen_height, self.screen_width, self.monkeys_dict[self.monkeytype])
        self.scene.handler = self
        if scene == "HARD2_SCENE":
            self.scene = Hard2Scene(self.screen_height, self.screen_width, self.monkeys_dict[self.monkeytype])
        self.scene.handler = self
