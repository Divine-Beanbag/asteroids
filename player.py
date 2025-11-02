import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS) #likely coming from constants.py via main.py
        self.rotation = 0 

    def triangle(self): #Player looks like triangle but has a circle hitbox for ease 
        self.forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + self.forward * self.radius
        b = self.position - self.forward * self.radius - self.right 
        c = self.position - self.forward * self.radius + self.right 
        return [a, b, c]

    def draw(self, screen):
        self.screen = screen
        pygame.draw.polygon(self.screen, WHITE, self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED *  dt)
        return self.rotation

    def move(self, dt):
        self.position += (self.forward * PLAYER_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys [pygame.K_d]:
            self.rotate(dt)
        if keys [pygame.K_w]:
            self.move(dt)
        if keys [pygame.K_s]:
            self.move(-dt)