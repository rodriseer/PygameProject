import pygame
from Platform import Platform
from Plaeyr import Player

class MainScreen:
    def __init__(self, width, height, name):
        # initialize pygame screen
        pygame.init()
        """
        Variables for height, and width of the screen
        If values are not valid, then prygame will try to fit the whole screen. Try to avoid this!
        """
        self._width = width
        self._height = height
        self.screen_name = name
        self._screen = pygame.display.set_mode((self._width, self._height))
        self._title = pygame.display.set_caption((name))
    
    @property
    def screen(self):
        """return main screen visualization"""
        return self._screen
    
    @screen.setter
    def screen(self, value, name):
        self._width, self._height = value
        self._screen  = pygame.display.set_mode(value)
        self._title =pygame.display.set_caption(name)

if __name__ == "__main__":
    # set size of screen according to preference
    main_screen = MainScreen(800, 600, "Chrono Slayer")

    # load background texture instead of pitch black screen
    background_texture = pygame.image.load(r"C:\Users\rodri\OneDrive\Área de Trabalho\PygamePlatformer\sprites\tilesets\floors\wooden.png")
    background_texture = pygame.transform.scale(background_texture, (main_screen._width, main_screen._height))

    # for top and bottom
    platform = Platform(800, 30, texture_path= r"C:\Users\rodri\OneDrive\Área de Trabalho\PygamePlatformer\sprites\tilesets\grass.png")
    # for left and right
    platform_vertical = Platform(30, 250, texture_path=r"C:\Users\rodri\OneDrive\Área de Trabalho\PygamePlatformer\sprites\tilesets\grass.png")
    platform_vertical_right = Platform(30, 600, texture_path=r"C:\Users\rodri\OneDrive\Área de Trabalho\PygamePlatformer\sprites\tilesets\grass.png")

    # if texture pack dont work refer to solid color: platform = Platform(600, 50, color=(0, 40, 0))

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill screen with black
        main_screen.screen.blit(background_texture, (0, 0))
        # draw platform with texture or color depending on init
        # bottom (full)
        platform.draw(main_screen.screen, 0, 570)
        # top (full)
        platform.draw(main_screen.screen, 0, 0)
        # left (left side is open in middle)
        platform_vertical.draw(main_screen.screen, 0, 0)
        platform_vertical.draw(main_screen.screen, 0, 350)
        # right (full right side)
        platform_vertical_right.draw(main_screen.screen,770, 0)

        player = Player()
        player.rect.x = 10
        player.rect.y = 10
        player_list = pygame.sprite.Group()
        player_list.add(player)




        pygame.display.flip()

    pygame.quit()