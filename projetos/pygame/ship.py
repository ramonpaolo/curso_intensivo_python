import pygame
class Ship():

    def __init__(self, screen):
        self.screen = screen

        #Carrega a imagem da espaçonave e obtém seu rect
        self.image = pygame.image.load("./imagem/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #inicia cada nova espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Desenha a espaçonave em sua posição atual"""
        self.screen.blit(self.image, self.rect)
