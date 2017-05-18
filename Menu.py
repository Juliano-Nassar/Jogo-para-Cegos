import pygame
from Voz import Falagg
    
fala = """Olá, seja bem vindo, você esta no Menu do melhor jogo da sua vida, só que não,kkk, vamos começar:
    escreva a opção escolhida
    se você quiser iniciar o jogo
    escreva iniciar
    se você quer fechar o jogo
    escreva fechar
    se você quiser entrar na lista de musicas do jogo
    escreva música"""

Falagg(fala)
while True:
    x = input(">")
    pygame.mixer.quit()
    if x == "iniciar" or x == "fechar":
        break
    
    else:
        fala = """Comando inválido, tente mais uma vez"""
        Falagg(fala)
if x == "iniciar":
    import Funcoes_Escolha as FE
    
    
elif x == "fechar":
    pass