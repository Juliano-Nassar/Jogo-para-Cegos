import pygame
from Voz import Falagg
import Criacao_arma as CA
import Luta as L
import Load
def comeco(Eu):
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
        return Forja1(Eu)#[Eu,0]
def Forja1(Eu):
    Falagg("""Você acorda, não se sabe quanto tempo passou, e você não escuta mais a floresta
    Você não sabe exatamente onde está e começa a procurar algo por perto, você tropeça e toca em um local do solo menos elevado
    será uma escada?
    em quanto você tenta descer com calma, sua mão esbarra em um corrimão,que estranho, que lugar é esse?
    você continua desccendo, parece uma escada sem fim.
    após algum tempo você chega no final e sente um calor escaldante, parabéns, encontrou sua primeira forja
    agora você podera criar uma arma""")
    Eu["arma"]= CA.Forja(["madeira","ferro","prata"])
    Falagg("""Você obteve {}, essa é sua primeira arma, cuide bem dela pois ela cuidara de você""".format(Eu["arma"].nome))
    return cavernaC(Eu)#[Eu,0]
    
def cavernaC(Eu):
    Falagg("""Saindo da forja,você  encontra duas paredes por perto,você decide:
        se quiser seguir a parede indo pela direita,
        digite direita
        se quiser seguir pela esquerda
        digite esquerda""")
    while True:
        escolha = input(">")
        if escolha == "direita":
            print("Você foi para a direita")
            return [Eu,1]
        elif escolha == "esquerda":
            print("Você foi para a esquerda")
            return [Eu,2]
        else:
            Falagg("Comando inválido, tente mais uma vez")
    
    

def cavernaC_Direita(Eu):
    Falagg("Você segue a parede por alguns metros.")
    Encontro(Eu)
    return Encontro(Eu)
    
def cavernaC_Esquerda(Eu):
    Falagg(("Você segue a parede por alguns metros e escuta uma borboleta."))
    
    return Encontro(Eu)
    
def Encontro(Eu):
    Falagg("""Você escuta um barulho estranho.
    o som das rapidas passadas aumentam, algo está correndo em sua direção
    Se prepare essa será sua primeira batalha
    Você está de frente com um ghuul, um ser místico que habita corpos mortos 
    Boa sorte!!""")
    L.Batalha(Load.enemy("Ghuul"),Eu)
    return[Eu,3]
