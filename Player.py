import pygame
import sys
import os

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        img = pygame.image.load(os.path.join('images', r'c:\Users\rodri\OneDrive\Área de Trabalho\PygamePlatformer\sprites\characters\player.png')).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
