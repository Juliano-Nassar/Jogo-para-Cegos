import pygame
from Voz import Falagg
def comeco():
    Falagg("""O barulho do cavalo cavalgando aumenta em quanto você corre daquele misterioso guerreiro
    no meio de toda essa confusão, uma correnteza de ar começa a ir á direita, com certeza isso deve ser uma caverna
    percebendo a oportunidade, você corre nesta direção e encosta nas paredes até encontrar uma entrada
    no meio desta noite tempestuosa e no desespero do misterioso cavaleiro te alcançar você corre seguindo a parede até que
   uma entrada é encontrada,procurando a sua volta você encontra correntes
   você:
       digite quebrar se quiser quebrar a corrente
       
       digite procurar se quiser seguir a corrente procurando por algo""")
    while True:
        escolha = input(">")
        pygame.mixer.quit()
        if escolha == "quebrar":
            Falagg("""Você puxa as correntes com toda a sua força,As correntes ,que a muito tempo não são tocadas, quebram facilmente,fechando o portão da entrada,salvando-o do perigo,
            mas você é arremessado para traz e cai no chão, desmaiando""")
        elif escolha == "procurar":
            Falagg("""Você segue as correntes até uma um objeto, percebendo que é uma alavanca, você tenta puxa-la para baixo, mas ela está enferrujada,dificultando seu trabalho, portanto usando toda sua força, você a consegue ativa-la
            ,fechando o portão e salvando-o do perigo,porem cai no chão, desmaiando""")
        else:
            Falagg("Comando inválido, tente mais uma vez")
        return
    
def cavernaC():
    Falagg("""Após algum tempo desmaiado,você se levanta e começa a tocar em tudo que está a sua volta
    você não escuta mais o lado de fora,consegue encontrar duas paredes por perto,você decide:
        se quiser seguir a parede indo pela direita,
        digite direita
        se quiser seguir pela esquerda
        digite esquerda""")
    while True:
        escolha = input(">")
        if escolha == "direita":
            return 0
        elif escolha == "esquerda":
            return 1
        else:
            Falagg("Comando inválido, tente mais uma vez")
    
        
    