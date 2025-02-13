from src.engine.game_engine import GameEngine
from src.entities.player import Player
from src.engine.hud import HUD
import pygame
from OpenGL.GL import *

class Game(GameEngine):
    def __init__(self):
        super().__init__()
        self.player = Player()
        self.hud = HUD()
        pygame.mouse.set_visible(False)
        
    def update(self):
        current_time = pygame.time.get_ticks() / 1000.0
        self.player.update(pygame.key.get_pressed(), current_time)
        
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Aplicar rotação da câmera
        glRotatef(self.player.rot[0], 1, 0, 0)
        glRotatef(self.player.rot[1], 0, 1, 0)
        glTranslatef(-self.player.pos[0], -self.player.pos[1], -self.player.pos[2])
        
        # Desenhar grade do chão
        self.draw_grid()
        
        # Render player/weapon
        self.player.render()
        
        # Render HUD
        self.switch_to_2d()
        self.hud.render(self.display, self.player.weapon)
        self.switch_to_3d()
        
        pygame.display.flip()
        self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()