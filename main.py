# Allows us to use code from open source pygame library
# throughout this file
import pygame
from constants import *
def main():
    pygame.init()
    
    # Creating a screen object using the pygame display.set_mode method
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    
    while(True):
        # Check if user has closed the window -> if so exits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Makes screen black
        screen.fill((0, 0, 0))

        
        # Refreshes the screen
        pygame.display.flip()

if __name__ == "__main__":
    main()


