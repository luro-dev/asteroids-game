from circleshape import *
from constants import *
import pygame
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0


    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen,"white", self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        # Stores true or false if respective key has been pressed
        keys = pygame.key.get_pressed()

        # Index is pygame named constant for respective key
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer <= 0:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN

        # Decreases player shoot cooldown, (prevents stream of shots)
        self.timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        # Used to create a shot at players position
        player_x = self.position.x
        player_y = self.position.y

        # Creates a shot at player position
        shot = Shot(player_x, player_y)

        # Rotates direction of vector to travel in plauer directon
        shot_vector = pygame.Vector2(0, 1)
        shot_vector = shot_vector.rotate(self.rotation)
        shot.velocity = shot_vector * PLAYER_SHOOT_SPEED


