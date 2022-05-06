import pygame


class Button:
    """Create a button, then blit the surface in the while loop"""

    def __init__(self, text, pos, font, bg="black"):
        self.x, self.y = pos                        # position of button
        self.font = pygame.font.Font("Assets/Luducudu.ttf", font) # Font of button
        self.change_text(text, bg)  # Text and background of button

    def change_text(self, text, bg="black"):
        """Change the text when you click"""
        self.text = self.font.render(text, 1, pygame.Color("White")) #what button will read
        self.size = self.text.get_size() # size of text
        self.surface = pygame.Surface(self.size)
        self.surface.fill(bg) #background colour of buttom
        self.surface.blit(self.text, (0, 0))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def render(self, screen): #render button onto screen
        screen.blit(self.surface, (self.x, self.y))

    def click(self, events):
        x, y = pygame.mouse.get_pos() #gets the coordinates of where mouse is
        for event in events:
            #checks to see if when mouse clicked is it colliding with button
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(x, y):
                return True
        return False
