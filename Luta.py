from random import randint
import Golpes

def Decidir(inimigo):
    qual = randint(len(inimigo["LA"]))
    print("{0} está prestes a usar {1}!".format(inimigo["nome"],inimigo["LA"][qual]))
    return qual

def Atacar(inimigo,Eu):
    hit = randint["1,100"]
    if hit >= (Eu["arma"].hit+inimigo["spd"]):
        Dmg = random.randint(Eu["arma"].attack) + Eu["atk"]
        inimigo["hp"] -= Dmg
        #som da arma
        print("Você acertou!")
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
        print("Você errou! Ha ha!")
        return inimigo,Eu,0

def Defender(inimigo,Eu):
    Eu["defesa"] = True
    print("Você se defendeu!")
    return inimigo,Eu,1

def Fugir(inimigo,Eu):
    if inimigo["Raridade"] =="boss":
        chance = 0
    else:
        chance = Eu["spd"] - inimigo["spd"]
    x = randint(1,Eu["spd"])
    if x <= chance:
        return inimigo,Eu,1
    else:
        return inimigo,Eu,0
    
def Especial(inimigo,Eu):
    return Eu["arma"].esp(inimigo,Eu)

def Batalha(inimigo,Eu):
    fuga = 0
    while inimigo["hp"]>0 and Eu["hp"] >0 and  fuga == 0:
        inimigo["golpe"] = Decidir(inimigo)
        comandos = ["Atacar","Especial","Defender","Fugir"]
        cmd = "aaa"
        while cmd not in comandos:
            cmd = input("O que você quer fazer?")
            if cmd not in comandos:
                print("Esse não é um comando valido")
        exec("outcome = Golpes.({}.title())(inimigo,Eu)".format(cmd))
        inimigo = outcome[0]
        Eu = outcome[1]
        fuga = outcome[2]
        if fuga == 1:
            break
        exec("out = {}(inimigo,Eu)".format(inimigo["golpe"]))
        inimigo = out[0]
        Eu = out[1]
        Eu["defesa"] = False
        if inimigo["hp"]/inimigo["mhp"] > 0.9:
            print("{} ainda está em bom estado.".format(inimigo["nome"]))
        if inimigo["hp"]/inimigo["mhp"] > 0.7:
            print("{} está um pouco machucado.".format(inimigo["nome"]))
        if inimigo["hp"]/inimigo["mhp"] > 0.5:
            print("{} está começando a se cançar.".format(inimigo["nome"]))
        if inimigo["hp"]/inimigo["mhp"] > 0.3:
            print("{} está abalado.".format(inimigo["nome"]))
        if inimigo["hp"]/inimigo["mhp"] > 0.1:
            print("{} está ferido.".format(inimigo["nome"]))
        else:
            print("{} está perto da morte.".format(inimigo["nome"]))
        if Eu["hp"]/Eu["mhp"] > 0.9:
            print("Você ainda está bem.".format(inimigo["nome"]))
        if Eu["hp"]/Eu["mhp"] > 0.7:
            print("Você está com alguns arranhões.".format(inimigo["nome"]))
        if Eu["hp"]/Eu["mhp"] > 0.5:
            print("Você está muito dolorido.".format(inimigo["nome"]))
        if Eu["hp"]/Eu["mhp"] > 0.3:
            print("Você está muito machucado.".format(inimigo["nome"]))
        if Eu["hp"]/Eu["mhp"] > 0.1:
            print("Você está bem mal.".format(inimigo["nome"]))
        else:
            print("Você está quase morrendo.".format(inimigo["nome"]))
    return