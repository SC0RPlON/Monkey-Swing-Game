import pygame

#class for tree
class Tree(pygame.sprite.Sprite):
    def __init__(self, x, y, position, gap):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/tree.png') #image of tree
        self.rect = self.image.get_rect() #makes image have rectangle
        self.gap = gap #gap between tree
        # position 1 will be top, -1 will be bottom
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(gap / 2)]

    def update(self, scroll_speed=3):
        self.rect.x -= scroll_speed #reduces x coordinate for a given duration
        if self.rect.right < 0:
            self.kill()  # destroys Tree off screen towards left of monkey saving memory space

