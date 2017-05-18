from random import randint
from time import sleep
import Golpes
import os

def Decidir(inimigo):
    qual = randint(1,len(inimigo["LA"])-1)
    print("{0} está prestes a usar {1}!".format(inimigo["nome"],inimigo["LA"][qual]))
    return inimigo["LA"][qual]

def Atacar(inimigo,Eu):
    hit = randint(1,100)
    if hit >= (Eu["arma"].hit+inimigo["spd"]):
        Dmg = randint((Eu["arma"].attack)[0],(Eu["arma"].attack)[1]) + Eu["atk"]
        inimigo["hp"] -= Dmg
        sleep(3)
        #som da arma
        print("Você acertou!")
        sleep(3)
        if Dmg < 5:
            print("O golpe fez pouco efeito!")
        elif Dmg < 10:
            print("Foi um golpe razoavel!")
        elif Dmg < 15:
            print("O golpe inflingiu um dano decente!")
        elif Dmg < 20:
            print("Foi um bom golpe!")
        elif Dmg < 25:
            print("Um acerto poderoso!")
        else:
            print("Uau! O inimigo sentiu isso!")
        return inimigo,Eu,0
    else:
        #som de erro
        sleep(2)
        print("Você errou! Ha ha!")
        return inimigo,Eu,0

def Defender(inimigo,Eu):
    Eu["defesa"] = True
    print("Você se defendeu!")
    sleep(1)
    return inimigo,Eu,1

def Fugir(inimigo,Eu):
    if inimigo["Raridade"] =="boss":
        chance = 0
    else:
        chance = Eu["spd"] - inimigo["spd"]
    x = randint(1,Eu["spd"])
    sleep(3)
    if x <= chance:
        print("Você fugiu!")
        return inimigo,Eu,1
    else:
        print("Você não conseguiu fugir!")
        return inimigo,Eu,0
    
def Especial(inimigo,Eu):
    return Eu["arma"].esp(inimigo,Eu)

def Batalha(inimigo,Eu):
    fuga = 0
    Eu["defesa"] = False
    inimigo["hp"] == inimigo["mhp"]
    os.system("cls")#ClearScreen
    while inimigo["hp"]>0 and Eu["hp"] >0 and  fuga == 0:
        inimigo["golpe"] = Decidir(inimigo)
        comandos = ["Atacar","Especial","Defender","Fugir"]
        cmd = "aaa"
        while cmd.title() not in comandos:
            for dvs in comandos:
                print(dvs)
            cmd = (input("O que você quer fazer?"))
            if cmd not in comandos:
                print("Esse não é um comando valido")
            os.system("cls")#ClearScreen
            if cmd.title() == "Atacar":
                outcome = Atacar(inimigo,Eu)
            if cmd.title() == "Defender":
                outcome = Defender(inimigo,Eu)
            if cmd.title() == "Especial":
                outcome = Especial(inimigo,Eu)
            if cmd.title() == Fugir:
                outcome = Fugir(inimigo,Eu)
            os.system("cls")#ClearScreen
                #exec("outcome = ({})(inimigo,Eu)".format(dvs))
        inimigo = outcome[0]
        Eu = outcome[1]
        fuga = outcome[2]
        if inimigo["hp"] <= 0:
            break
        if fuga == 1:
            break
        #exec("from Golpes import {}".format(inimigo["golpe"]))
        #exec("outp = {}(inimigo,Eu)".format(inimigo["golpe"]))
        os.system("cls")#ClearScreen
        outp = getattr(Golpes, inimigo["golpe"])(inimigo,Eu)
        os.system("cls")#ClearScreen
        inimigo = outp[0]
        Eu = outp[1]
        Eu["defesa"] = False
        sleep(2)
        if  Eu["hp"] <= 0:
            break
        if inimigo["hp"]/inimigo["mhp"] > 0.9:
            print("{} ainda está em bom estado.".format(inimigo["nome"]))
        elif inimigo["hp"]/inimigo["mhp"] > 0.7:
            print("{} está um pouco machucado.".format(inimigo["nome"]))
        elif inimigo["hp"]/inimigo["mhp"] > 0.5:
            print("{} está começando a se cansar.".format(inimigo["nome"]))
        elif inimigo["hp"]/inimigo["mhp"] > 0.3:
            print("{} está abalado.".format(inimigo["nome"]))
        elif inimigo["hp"]/inimigo["mhp"] > 0.1:
            print("{} está ferido.".format(inimigo["nome"]))
        else:
            print("{} está perto da morte.".format(inimigo["nome"]))
        sleep(2)
        if Eu["hp"]/Eu["mhp"] > 0.9:
            print("Você ainda está bem.".format(inimigo["nome"]))
        elif Eu["hp"]/Eu["mhp"] > 0.7:
            print("Você está com alguns arranhões.".format(inimigo["nome"]))
        elif Eu["hp"]/Eu["mhp"] > 0.5:
            print("Você está muito dolorido.".format(inimigo["nome"]))
        elif Eu["hp"]/Eu["mhp"] > 0.3:
            print("Você está muito machucado.".format(inimigo["nome"]))
        elif Eu["hp"]/Eu["mhp"] > 0.1:
            print("Você está bem mal.".format(inimigo["nome"]))
        else:
            print("Você está quase morrendo.".format(inimigo["nome"]))
    if Eu["hp"]<= 0:
        print("Você morreu! Haha!")
        time.sleep(0.5)
        os._exit(0)
    elif inimigo["hp"]<=0:
        print("{} morreu! Você ganhou a batalha!".format(inimigo["nome"]))
    return Eu