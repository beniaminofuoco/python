# Python supporta sia l'ereditarietà singola che l'eereditarietà multipla
# Analizziamo un esempio di EREDITARIETA' SINGOLA:
# la classe BClass è la super classe della classe AClass
class BClass:
    pass

class AClass(BClass):
    pass

# Una classe però potrebbe essere sottoclasse di diverse super classi
# in questo caso stiamo parlando di EREDITARIETA' MULTIPLA
# Le classi BClass e CClass sono super classi di AClass
class BClass:
    b =10
    def bFunc(self):
        print("Sono nella classe BClass")

    def xFunc(self):
        print("Sono nella classe BClass")

class CClass:
    c =20
    def cFunc(self):
        print("Sono nella classe CClass")

    def xFunc(self):
        print("Sono nella classe CClass")

class AClass(BClass, CClass):
    pass

# Fino a qui tutto è stato semplice e lineare. Ma cosa succede se entrambe le classi,
# BClass e CClass, definiscono la stessa funzione xFunc ?
# Come vediamo nel main, il metodo stamperà "Sono nella classe BClass".
# Questo avviene utilizzando il criterio di MRO (Method Resolution Order).
# MRO va prima a cercare la funzione xFunc nella classe AClass, se non la trova xFunc
# risale la gerarchia delle super classi iniziando a cercare nella prima superclasse (BClass)
# e qualora non la trovasse continuerebbe a cercare nella seconda superclasse (CCLass).
# Qualora non trovasse la funzione in nessuna delle superclassi, MRO andrebbe a cercare nella
# classe Object

if __name__ == "__main__":
    a = AClass()
    print(a.b) # Stamperà 10
    print(a.c) # Stamperà 20
    print()
    a.bFunc() # Stamperà "Sono nella classe BClass"
    a.cFunc() # Stamperà "Sono nella classe CClass"
    print()
    a.xFunc() # Stamperà "Sono nella classe BClass"