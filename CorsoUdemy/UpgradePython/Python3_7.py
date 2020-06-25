# PEP -> Python Enhancement Proposals, cioè è una proposta di miglioramento del linguaggio Python
# Nel corso degli anni sono state introdotte diverse PEP che definiscono le Type Annotation:
# PEP 3107 -> Function Annotations, introduce la possibilità di annotare i parametri
#             e i valori di ritorno di una funzione.
#             Es. di sintassi:  def func(a: expression, b: expression): -> expression:
#
# PEP 484 -> Type Hints, utilizza la sintassi delle Function Annotations per specificare il tipo
#            nei parametri e nel return. Qui di seguito abbiamo specificato che x è di tipo int
#            e che s è di tipo stringa. Infine abbiamo specificato il tipo di ritorno
#            def myFunc(x: int, s: str ="pyhton") -> str:
#               print(x)
#               return s
#
#           print(myFunc(10)) stamperà ->  10 python
# PEP 526 -> Syntax for Variable Annotations, si estende l'utilizzo del Type anche alle variabili
#           a: int = 10

# La versione 3.7 di Python è stata rilasciata nel 2018 e ha introdotto i seguenti miglioranti:
# - L'ordinamento delle chiavi all'interno di un Dizionario garantisce l'ordine di inserimento
# - I Type Hints

class Python3_7:
    # Usiamo l'annotation Type per le variabili
    a: int=10

    # Abbiamo definito due variabili d'istanza specificando il Type
    nome: str
    cognome: str

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    @staticmethod
    def myFunc(x: int, s: str = "pyhton") -> str:
        print(x)
        return s



if __name__ == "__main__":
    myDict = {"primo":10, "secondo":20, "terzo":30}
    myDict["quarto"] = 40
    # Come possiamo vedere l'ordine di inserimento è stato mantenuto
    print(myDict.keys()) # dict_keys(['primo', 'secondo', 'terzo', 'quarto'])

    print()

    # Test PEP 484
    print(Python3_7.myFunc(10)) #  stamperà ->  10 python

    print()

    # Stamperà il contenuto dei Type Hints
    # Queste informazioni vengono utilizzate dai tool per effettuare dei controlli di congruenza dei dati
    print(Python3_7.myFunc.__annotations__) # {'x': <class 'int'>, 's': <class 'str'>, 'return': <class 'str'>}

    print()

    print(Python3_7.a) # 10
    print(Python3_7.__annotations__) # {'a': <class 'int'>}