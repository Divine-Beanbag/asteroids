import pygame
from constants import *
from player import *
from circleshape import *


def main():
    pygame.init() # initialize pygame  
    pygame.display.set_caption(WINDOW_BANNER)#Text at tope of window 
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #create a display surface
    clock = pygame.time.Clock() #setting framerate
    dt = 0
   
    updatable_group = pygame.sprite.Group() # stuff I use the update method on
    drawable_group = pygame.sprite.Group() # stuff I use the draw method on 
    Player.containers = (updatable_group, drawable_group) #make each group a container for  all Player instances 
    Player(x_pos, y_pos)

  #the player object 
    
    # group.update() calls the method for every member of the group 
    #   e.g. group_a.update(dt)
    # calling a method "on something" add it to the beginning with a period.
    # "using something as an argument" put it inside the parenthesis 
    
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
        updatable_group.update(dt)

        #render graphics here 
        for drawable in drawable_group:
            drawable.draw(screen)

        pygame.display.flip() #Call last! Use display.flip to update the display

        
if __name__ == "__main__":
    main()
