'''
SceneHandler Abstract class

methods:
    - go
        - This goes to a Scene

'''



class SceneHandler(object):
    def __init__(self):
        raise NotImplementedError

    def go(self, scene):
        raise NotImplementedError