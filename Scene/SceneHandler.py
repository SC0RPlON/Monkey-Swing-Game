'''
SceneHandler Abstract class

methods:
    - go
        - This goes to a Scene

'''
from Scene.GameScene import GameScene
from Scene.MainScene import MainScene


class SceneHandler(object):
    def __init__(self):
        self.go("MAIN_SCENE")

    def go(self, scene):
        if scene == "GAME_SCENE":
            self.scene = GameScene()
        if scene == "MAIN_SCENE":
            self.scene = MainScene()
        self.scene.handler = self