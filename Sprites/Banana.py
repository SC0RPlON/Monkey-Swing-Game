import pygame

#class for banana
class Banana(pygame.sprite.Sprite):
    def __init__(self, y, x, scroll_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/banana.png') #image for banana
        self.rect = self.image.get_rect() #rectangle for banana
        self.rect.bottomleft = [x, y] #given position for bottom left of banana
        self.scroll_speed = scroll_speed

    def update(self):
        self.rect.x -= self.scroll_speed
        if self.rect.right < 0:
            self.kill()  # destroys bananas off screen towards left of monkey saving memory space
