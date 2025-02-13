import pygame
from .weapon import Weapon
import math

class Player:
    def __init__(self, pos=[0,0,-5]):
        self.pos = list(pos)
        self.rot = [0, 0]  # pitch, yaw
        self.speed = 0.1
        self.weapon = Weapon()
        self.mouse_sensitivity = 0.2
        pygame.mouse.get_rel()  # Reseta o movimento do mouse
        
    def update(self, keys, current_time):
        # Mouse look
        mouse_dx, mouse_dy = pygame.mouse.get_rel()
        self.rot[0] = min(89, max(-89, self.rot[0] - mouse_dy * self.mouse_sensitivity))
        self.rot[1] = (self.rot[1] + mouse_dx * self.mouse_sensitivity) % 360
        
        # Movimento relativo à direção do olhar
        forward = math.cos(math.radians(self.rot[1]))
        right = math.sin(math.radians(self.rot[1]))
        
        if keys[pygame.K_w]:
            self.pos[0] -= right * self.speed
            self.pos[2] -= forward * self.speed
        if keys[pygame.K_s]:
            self.pos[0] += right * self.speed
            self.pos[2] += forward * self.speed
        if keys[pygame.K_a]:
            self.pos[0] -= forward * self.speed
            self.pos[2] += right * self.speed
        if keys[pygame.K_d]:
            self.pos[0] += forward * self.speed
            self.pos[2] -= right * self.speed
            
        # Pulo/Agachamento
        if keys[pygame.K_SPACE]:
            self.pos[1] += self.speed
        if keys[pygame.K_LSHIFT]:
            self.pos[1] -= self.speed
            
        # Atirar
        if pygame.mouse.get_pressed()[0]:  # Botão esquerdo
            self.weapon.shoot(self, current_time)
            
    def render(self):
        self.weapon.render()