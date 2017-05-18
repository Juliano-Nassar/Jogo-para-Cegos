import Criacao_arma as ca
import Luta
import json

def enemy(nome):
	with open("Inimigos.json","r") as ini:
		Inim = json.load(ini)
	return Inim[nome]


Player = {"mhp":30,"arma":(ca.Arma("Edge","madeira","prata","ferro")),"hp":30,"atk":3,"def":3,"spd":3}

Luta.Batalha(enemy("Ghuul"),Player)