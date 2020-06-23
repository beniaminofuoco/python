# Come abbiamo visto, per inizializzare i parametri di una classe abbiamo utilizzato
# il metodo __init__. Questo metodo però non è il costruttore di una classe, ma un inizializzatore.

# Il vero costruttore di una classe è il metodo __new__, che verrà SEMPRE richiamato PRIMA del metodo __init__
# Il metodo __init__ riceve in ingresso un'istanza di un oggetto, ritornata proprio dal metodo __new__,
# e su questa istanza inizializzerà i vari parametri.
class MyClass1:
    def __new__(cls):
        print("Istanza Creata!")
    def __init__(self):
        print("Istanza Inizializzata")


class MyClass2:
    def __new__(cls):
        istanza = super().__new__(cls)
        print("Istanza Creata!")
        return istanza
    def __init__(self):
        print("Istanza Inizializzata")

class MyClass3:
    def __new__(cls,message):
        istanza = super().__new__(cls)
        print("Istanza Creata!")
        return istanza
    def __init__(self, message):
        print("Istanza Inizializzata -> ", message)


if __name__ == "__main__":
    obj1 = MyClass1()
    #"Istanza Creata!" -> cioè viene chiamato solo il metodo __new__

    print()

    obj2 = MyClass2()
    # "Istanza Creata!" -> prima viene richiamato il costruttore __new__
    # "Istanza Inizializzata"-> e subito dopo l'oggetto "istanza" viene passato al metodo __init__ come oggetto self

    print()

    obj3 = MyClass3("Python")
    # "Istanza Creata!" -> prima viene richiamato il costruttore __new__
    # "Istanza Inizializzata -> Python" -> viene passato l'istanza della classe MyClass3 e il parametro message