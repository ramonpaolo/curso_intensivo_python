import sys
import pygame
from configuracao import Settings
from ship import Ship

def run_game():
    pygame.init()
    configuracao = Settings()
    screen = pygame.display.set_mode((configuracao.screen_width, configuracao.screen_height))
    pygame.display.set_caption(configuracao.title)
    ship = Ship(screen)
    cor = (230, 230, 230)

    while True:

        #Observa os eventos de teclado e mouse
        for evento in pygame.event.get():

            #Quando o usuário clicar para fechar a janela
            if evento.type == pygame.QUIT:
                #Sair do jogo
                sys.exit()

        ship.blitme()

        #Define a cor do fundo(dos 1200 por 800)
        screen.fill(configuracao.cor)

        #Faz com que quando a tela seja atualizada faça uma atualização a tela com os objetos
        pygame.display.flip()


run_game()