import pygame
from Voz import Falagg
import Load
import json
import Criacao_arma as CA
   
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
    
    with open("Save.json", "r") as sav:
        Save = json.load(sav)
        if Save == {}:
            Load.Newgame()
        else:
            Falagg("Se quiser começar um novo jogo escreva novo,se quiser continuar, escreva continuar")
            escreva = input("> ")
            if escreva == "novo":
                Load.Newgame()
    Eu = Load.player()
    Eu["arma"]=CA.Arma(Eu["armad"][0],Eu["armad"][1],Eu["armad"][2],Eu["armad"][3])
    while True:
        import Funcoes_Escolha as FE
        lista=["comeco","cavernaC_Direita","cavernaC_Esquerda"]
        Eu["arma"]=CA.Arma(Eu["armad"][0],Eu["armad"][1],Eu["armad"][2],Eu["armad"][3])
        outcome = getattr(FE,lista[Load.place()])(Eu)
        Eu = outcome[0]
        pos = outcome[1]
        Falagg("""Você quer coninuar a jogar ou quer sair?
        Cuidado, seu jogo só sera salvo após escolhas""")
        opt = input("")
        Load.Save(Eu,pos,{})
        if opt.lower() == "sim":
            break
        
        
    
    
    
    
elif x == "fechar":
    pass