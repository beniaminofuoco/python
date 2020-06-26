# La PEP 572 introduce le Assignment Expression
# Le Assignment Expressions sono indentificate dall'operatore Walrus (Tricheco) Operator :=
class AssignmentExpression:
    pass

if __name__ == "__main__":

    def somma(a, b):
        return a+b

    # if x = somma(3,5) > 6 -> senza operatore Walrus andrebbe in errore
    if x := somma(3,5)>6:
        print("Somma maggiore di 6")

    print()

    # Tutto ciò vale anche per l'utilizzo di altre funzioni predefinite
    myList = [1,2,3,4,5]
    while x := len(myList) != 0:
        print(x, myList.pop())

    # Il ciclo stamperà:
    #True 5
    #True 4
    #True 3
    #True 2
    #True 1
    print()

    # x := somma(3, 5) -> ERRORE, le Assignment Expression non sono valide al primo livello
    # Per ovviare a ciò è necessario racchiuderle tra parentesi.
    (x := somma(3,5))
    print(x) #8
    print()

    def saluta1(nome = "Susanna"):
        print("Ciao ", nome)

    saluta1() # Ciao Susanna
    print()

    # def salutaError(nome= n := "Susanna")-> ERRORE, l'operatore Walrus deve essere racchiuso tra parentesi
    def salutaOk(nome = (n:="Susanna")):
        print("Ciao ", nome)
        print("Ciao ", n.upper()) # Stamperà il valore del parametro n in upper case

    salutaOk()
    # Stamperà:
    # Ciao Susanna
    # Ciao SUSANNA

    print()
    salutaOk("Beniamino")
    # Stamperà:
    # Ciao Beniamino
    # Ciao SUSANNA -> il valore di default verrà comunque stampato