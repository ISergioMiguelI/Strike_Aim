from OpenGL.GL import *
import numpy as np

class Bullet:
    def __init__(self, pos, direction):
        self.pos = pos
        self.direction = direction
        self.speed = 0.5
        self.lifetime = 100
        
    def update(self):
        self.pos[0] += self.direction[0] * self.speed
        self.pos[1] += self.direction[1] * self.speed
        self.pos[2] += self.direction[2] * self.speed
        self.lifetime -= 1
        
    def render(self):
        glPushMatrix()
        glTranslatef(*self.pos)
        # Desenhar esfera simples
        glutSolidSphere(0.1, 10, 10)
        glPopMatrix()