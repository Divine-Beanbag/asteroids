import pygame
from constants import *
from player import *
from circleshape import *


def main():
    pygame.init() # initialize pygame 
    # set up the display 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a display surface
    clock = pygame.time.Clock()
    caption = pygame.display.set_caption("All hail the Divine Beanbag!")
    dt = 0
    x_pos = SCREEN_WIDTH / 2
    y_pos = SCREEN_HEIGHT / 2
    player_pos = Player(x_pos, y_pos)
    

 #Game loop
    while True:
        dt = clock.tick(60)/100

        # Process player inputs 
        for event in pygame.event.get(): #user does a thing
            if event.type == pygame.QUIT: # user clicks close button
                pygame.quit() # close the gameplay loop
                raise SystemExit

        #do logical updates here 
        screen.fill(BLACK) #fill the screen with black color

        #render graphics here 
        player_pos.draw(screen)
        pygame.display.flip() #Call last! Use display.flip to update the display


       
    
    
    
    # Game loop
    # Check for player inputs
    # Update game
    # Draw game to screen

    

    
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


        
if __name__ == "__main__":
    main()
