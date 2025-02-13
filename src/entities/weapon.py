from OpenGL.GL import *
import pygame

class Weapon:
    def __init__(self):
        self.ammo = 30
        self.max_ammo = 30
        self.fire_rate = 0.5  # segundos entre tiros
        self.last_shot = 0
        self.recoil = 0
        self.damage = 100
        
    def shoot(self, player, current_time):
        if current_time - self.last_shot >= self.fire_rate and self.ammo > 0:
            self.ammo -= 1
            self.last_shot = current_time
            self.recoil = 0.2
            return True
        return False

    def render(self):
        glPushMatrix()
        # Posição da arma na tela
        glTranslatef(0.4, -0.3 - self.recoil, -0.5)
        glRotatef(-90, 0, 1, 0)
        glScalef(0.1, 0.1, 0.1)
        
        # Renderização básica
        glColor3f(0.5, 0.5, 0.5)  # Cor cinza
        glBegin(GL_QUADS)
        # ... desenho básico da arma
        glEnd()
        
        glPopMatrix()
        
        # Reduz o recuo gradualmente
        self.recoil = max(0, self.recoil - 0.01)