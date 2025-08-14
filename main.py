# Allows us to use code from open source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")

    pygame.init()
    
    # Creating a screen object using the pygame display.set_mode method
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # Creates a Clock object to keep track of gametime
    clock = pygame.time.Clock()
    dt = 0


    # Creating groups to update and draw
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    
    # Set the groups as containers for the player, and for the asteroids and its field
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)


    # Creates player object, and asteroid field
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while(True):
        # Check if user has closed the window -> if so exits game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Makes screen black
        screen.fill((0, 0, 0))

        # Re-render player on the screen each frame (added groups for all updateable things)
        updateable.update(dt)

        # Check for collision between astr and shots
        # Check if there were any collisions between plyr and astr
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()

            if asteroid.collision_check(player):
                print("Game over!")
                return

        for thing in drawable:
            thing.draw(screen)

        # Refreshes the screen
        pygame.display.flip()

        # Sets the framerate to 60FPS and stores time since last call in seconds
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()


