import pygame

class Platform:
    def __init__(self, width, height, color = (255, 255, 255), texture_path=None):
        self._width = width
        self._height = height
        self._color = color
        self._platformMain = pygame.Surface((self._width, self._height))

        # creating a flag to signal if any texture pack is present
        if texture_path:
            # if a texture pack is provided, load and scale the pack
            self._texture = pygame.image.load(texture_path)
            self._texture = pygame.transform.scale(self._texture, (self._width, self._height))
            # if teture is on, bool to true to flag texture pack
            self._use_texture = True
        else:
            # otherwise, fill with the solid color
            self.platformMain.fill(self._color)
            # bool to false, no textre used
            self._use_texture = False

    @property
    def platform(self):
        """return the surface"""
        return self._platformMain

    @platform.setter
    def platform(self, size):
        self._width, self._height = size
        self._platformMain = pygame.Surface(size)
        self._platformMain.fill(self._color)
    
    def draw(self, screen, x, y):
        """draw the platform at the given (x, y) position on the screen"""
        # flag to signal which drawing to display
        if self._use_texture:
            screen.blit(self._texture, (x, y))
        else:
            screen.blit(self._platformMain, (x, y))