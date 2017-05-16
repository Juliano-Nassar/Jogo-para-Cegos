from random import randint

Mat = {"ferro":{"pow":5,"peso":6,"ins":4},"prata":{"pow":2,"peso":2,"ins":6},"madeira":{"pow":3,"peso":3,"ins":2}}
#Classe de arma
class Arma():
    def __init__(self,nome,mat1,mat2,mat3):
        tack = Mat[mat1["pow"]]+Mat[mat2["pow"]]+mat3["pow"]
        inst = Mat[mat1["ins"]] +Mat[mat2["ins"]] +Mat[mat3["inst"] ]
        self.attack = [tack-inst,tack+inst]
        self.hit  = Mat[mat1["hit"]] + Mat[mat2["hit"]] + Mat[mat3["hit"]]
        self.peso = Mat[mat1["peso"]] + Mat[mat2["peso"]] + Mat[mat3["peso"]]
        #self.som = Mat[mat3["som"]]
        
    def Dano():
        dano = randint(self.attack[0],self.attack[0]+1)
        return d
        
def Forja(Listamat):
    x = []
    nome = input("Qual será o nome da sua arma?")
    for n in ["cabo","guarda","lamina"]:
        a = "aaa"
        while a not in Listamat:
            a = ("De que material será feita a {}".format(n))
            if a not in Listamat:
                print("Esse não é um material valido.")
        x.append(a)
    arm = Arma(nome,x[0],x[1],x[2])
    return arm     