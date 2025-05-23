import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, color=(255, 255, 255), radius=self.radius, width=2, center=self.position)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        
        split_delta =  random.uniform(20, 50)
        
        new_r = self.radius - ASTEROID_MIN_RADIUS
        ast_1 = Asteroid(self.position.x, self.position.y, new_r)
        ast_2 = Asteroid(self.position.x, self.position.y, new_r)
        ast_1.velocity = self.velocity.rotate(split_delta * -1)
        ast_2.velocity = self.velocity.rotate(split_delta*2)