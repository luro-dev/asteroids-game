import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision_check(self, circle_shape_object):
        distance_between_each = self.position.distance_to(circle_shape_object.position)
        combined_radius = self.radius + circle_shape_object.radius

        # If the sum of the radius of each circle is greater than than or equal to the distance they are
        # colliding 
        if combined_radius >= distance_between_each:
            return True
        else:
            return False


