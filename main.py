import pygame

from Scene.MainScene import MainScene
from Scene.SceneHandler import SceneHandler


def main():
    '''
    - Initialise Pygame <-
    - Load up main menu <-
    - Check if the buttons pressed
    - Redirect to different scenes
    '''
    pygame.init()
    clock = pygame.time.Clock()
    fps = 60
    screen_width = 864
    screen_height = 936
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Swing Monkey Swing')

    # Scene is the curerntly rendering scene
    handler = SceneHandler()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)

        handler.scene.handle(pygame.event.get())
        handler.scene.update()
        handler.scene.render(screen)
        pygame.display.update()
    pygame.quit()




if __name__ == "__main__":
    main()