from random import randint
from time import sleep

def calchit(a,d,hit):
    hts = randint(0,99)
    if hts >= (hit+d["spd"]):
    	return True
    else:
    	return False

def defesa(golpe,defesa):
	if defesa == True:
		print("Você se defendeu!")
		sleep(2)
		return golpe /2
	else:
		return golpe

def mordida(a,d):
	hit = 20
	h = calchit(a,d,hit)
	if h == True:
		dm = [3,9]
		Dmg = randint(dm) + a["atk"]
		Dmg = defesa(Dmg,d["defesa"])
		d["hp"] -= Dmg
		print("{} te mordeu!".format(a["nome"]))
		sleep(3)
		if Dmg <= 5:
			print("Mas ele não rasgou a sua pele!")
		elif Dmg <= 15:
			print("A mordida fez você sangrar!")
		elif Dmg <= 25:
			print("A mordida rasgou a sua carne!")
		else:
			print("Você tem sorte de não ter perdido um braço com uma mordida dessas!")
	if h == False:
		print("{} não conseguiu te morder!".format(a["nome"]))
		sleep(3)
	return a,d

def agarrar(a,d):
	hit = 20
	h = calchit(a,d,hit)
	if h == True:
		dm = [7,14]
		Dmg = randint(dm) + a["atk"]
		Dmg= defesa(Dmg,d["defesa"])
		d["hp"] -= Dmg
		print("{} te agarrou!".format(a["nome"]))
		sleep(3)
		if Dmg <= 5:
			print("Mas você conseguiu se desvincilhar rapidamente e sofreu poucos danos!")
		elif Dmg <= 15:
			print("Você foi cortado por suas garras!")
		elif Dmg <= 25:
			print("A força do aggarrão causou muita dor!")
		else:
			print("Por pouco você não foi estrangulado pelo agarrão!")
	if h == False:
		print("{} tentou te agarrar, mas não conseguiu!".format(a["nome"]))
		sleep(3)
	return a,d