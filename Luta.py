from random import randint


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
    
    

def Batalha(inimigo,Eu):
    fuga = 0
    while inimigo["hp"]>0 and Eu["hp"] >0 and  fuga == 0:
        comandos = ["Atacar","Especial","Defender","Fugir"]
        cmd = "aaa"
        while cmd not in comandos:
            cmd = input("O que você quer fazer?")
            if cmd not in comandos:
                print("Esse não é um comando valido")
        outcome = cmd(inimigo,Eu)
        inimigo = cmd[0]
        Eu = cmd[1]
        fuga = cmd[2]
    return