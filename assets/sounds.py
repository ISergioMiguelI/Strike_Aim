import pygame

class Sounds:
    def __init__(self):
        pygame.mixer.init()  # Inicializa o mixer
        try:
            self.shoot_sound = pygame.mixer.Sound('assets/sounds/sniper_shot.wav')
        except:
            print("Erro ao carregar som")
            self.shoot_sound = None