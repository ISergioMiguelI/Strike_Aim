import pygame
from OpenGL.GL import *

class HUD:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
        
    def render(self, screen, weapon):
        ammo_text = f"Ammo: {weapon.ammo}/{weapon.max_ammo}"
        text_surface = self.font.render(ammo_text, True, (255, 255, 255))
        screen.blit(text_surface, (10, screen.get_height() - 40))