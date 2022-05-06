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
    screen_width = 718
    screen_height = 617
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('Swing Monkey Swing')

    # Scene is the currently rendering scene
    handler = SceneHandler(449, screen_width)

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
