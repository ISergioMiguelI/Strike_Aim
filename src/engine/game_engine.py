import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class GameEngine:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.width = width
        self.height = height
        self.display = pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Setup 3D
        glEnable(GL_DEPTH_TEST)
        glClearColor(0.5, 0.7, 1.0, 1.0)  # Cor do céu (azul claro)
        gluPerspective(45, (width/height), 0.1, 50.0)
    
    def draw_grid(self):
        glBegin(GL_LINES)
        glColor3f(0.5, 0.5, 0.5)  # Cor cinza
        
        # Grade horizontal
        for i in range(-10, 11):
            glVertex3f(-10, 0, i)
            glVertex3f(10, 0, i)
            glVertex3f(i, 0, -10)
            glVertex3f(i, 0, 10)
            
        glEnd()
    
    def switch_to_2d(self):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, self.width, self.height, 0, -1, 1)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glDisable(GL_DEPTH_TEST)
        
    def switch_to_3d(self):
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)
        glEnable(GL_DEPTH_TEST)
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False
                
    def update(self):
        pass
        
    def render(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pygame.display.flip()
        
    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)
        pygame.quit()