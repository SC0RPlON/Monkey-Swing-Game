'''
Scene Abstract class

methods:
    - render
        - This draws entities onto the screen
    - handle
        - This will help with going to different screens
    - update
        - This constantly checks for animations, gravity, character swinging and jumping

'''

class AbstractScene(object):
    def __init__(self):
        pass

    def render(self, screen):
        pass

    def handle(self, events):
        pass

    def update(self):
        pass

