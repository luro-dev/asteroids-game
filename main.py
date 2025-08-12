# Allows us to use code from open source pygame library
# throughout this file
import pygame
from constants import *
def main():
    print("Starting Asteroids!")

    pygame.init()
    
    # Creating a screen object using the pygame display.set_mode method
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Creates a Clock object to keep track of gametime
    clock = pygame.time.Clock()
    dt = 0

    while(True):
        # Check if user has closed the window -> if so exits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Makes screen black
        screen.fill((0, 0, 0))

        
        # Refreshes the screen
        pygame.display.flip()

        # Sets the framerate to 60FPS and stores time since last call in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


