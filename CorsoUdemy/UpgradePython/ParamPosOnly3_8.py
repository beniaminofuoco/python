# PEP 570 - Python Positional-Only Parameters
# Questa PEP ci permette di specificare, attraverso l'operatore /, che alcuni parametri non possono
# essere di tipo Keyword ma devono essere SEMPRE posizionali.
class PositionalOnlyParam:
    pass

if __name__ == "__main__":

    def somma(a,b,c):
        return a+b+c

    # Richiamo lo funzione assegnando dei parametri posizionali
    print(somma(10, 4, 2)) # 16
    print()

    #Richiamo la funzione assegnando dei parametri keyword
    print(somma(b=4, c=2, a=10)) # 16
    print()


    # Indico che il parametro a deve essere sempre posizionale
    def sommaParmOnlyPos(a,/, b, c):
        return a + b + c

    # print(sommaParmOnlyPos(b=4, a=10, c=2))
    # Ottengo il seguente errore:
    # sommaParmOnlyPos() got some positional-only arguments passed as keyword arguments: 'a'

    print(sommaParmOnlyPos(10, c=2, b=4)) # 16
