import pygame
pygame.init()
from constants import *

BLACK = (0, 0, 0, 1)


def main():
    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, BLACK) #fill the screen with black color 
        pygame.display.flip() #use display.flip to update the screen



if __name__ == "__main__":
    main()
