import Criacao_arma as ca
import Luta
import json

def enemy(nome):
	with open("Inimigos.json","r") as ini:
		Inim = json.load(ini)
	return Inim[nome]

def player():
	with open("Save.json","r") as sav:
		Sae = json.load(sav)
	return Sae["Eu"]

def place():
	with open("Save.json","r") as sav:
		Pae = json.load(pos)
	return Pae["pos"]

def Newgame():
	Sav = {"Eu":{"nome":"","mhp":30,"hp":30,"spd":5,"def":3,"atk":4},'pos':0,"inv":{}}
	with open("Save.json", "w") as Arq:
        json.dump(Sav,Arq)

def Save(player,loc,inv):
	player["arma"]=[player["arma"].nome,player["arma"].mat1,player["arma"].mat2,player["arma"].mat3]
	Sav = {"Eu":{"nome":"","mhp":30,"hp":30,"spd":5,"def":3,"atk":4},'pos':0,"inv":{}}
	with open("Save.json", "w") as Arq:
        json.dump(Sav,Arq)

Player = {"mhp":30,"arma":(ca.Arma("Edge","madeira","prata","ferro")),"hp":30,"atk":3,"def":3,"spd":3}

Luta.Batalha(Load.enemy("Ghuul"),Player)