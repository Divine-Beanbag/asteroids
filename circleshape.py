import pygame
from constants import *
from player import *

# Base class for game objects

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers) #if container attribute exists it calls the constructor with containers 
        else:
            super().__init__() #otherwise initialize the sprite with default behavior 

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius 

    def draw(self, screen):# screen variable may have changed 
        # sub-classes must override 
        pass

    def update(self, dt):
        # sub-casses must override 
        pass 