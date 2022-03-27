import pygame

class Monkey(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.game_over = False#
        self.swinging = True
        self.images = []
        self.index = 0 #first point of list so shows first image
        self.counter = 0 #controls speed of animation when running
        for num in range (1, 4):
            img = pygame.image.load('m1.png')
            #img = pygame.image.load(f'm{num}.png')#picture sprite will be assigned
            self.images.append(img) #appends image which has just been loaded
        self.image = self.images[self.index]
        self.rect = self.image.get_rect() #gets boundaries of image
        self.rect.center = [x, y]
        self.vel = 0
        self.click = False


    def update(self):
        if self.game_over == False:

        #gravity
            if self.swinging == True:
                self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        #jump
            if pygame.mouse.get_pressed()[0] == 1 and self.click == False: #looks for when mouse click has happened left click is 0 index
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #handle animation
            self.counter += 1 #increases counter by 1 each iteration
            flap_cooldown = 5

            if self.counter > flap_cooldown:

                self.counter = 0
                self.index += 1
            if self.index >= len(self.images):
                self.index = 0
                self.image = self.images[self.index]

        # rotate monkey
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
