# Un oggetto iterable è un oggetto che ritorna un iteratore, allo scopo di poter
# iterare sui propri oggetti. I container (List, Dictonary, etc) sono degli oggetti iterable.
# __iter()__

# Un oggetto che produce il prossimo elemento di una oggetto iterable è: __next()__

# Un oggetto può essere sia iterable (__iter()__) che un iterator (di se stesso)
# se implementa anche il metodo __next()__


# La  seguente classe realizza un iteratore che è anche iterable.
# Per far ciò deve implementare sia il metodo __iter()__ che il metodo __next()__
# Il nostro iteratore parte da due e ritorna il numero successivo moltiplicato per 2, fino a 300
class MyIterator:
    def __iter__(self):
        self.myAttr = 2
        return self

    def __next__(self):
        if self.myAttr < 300:
            n = self.myAttr
            self.myAttr *= 2
            return n
        else:
            raise StopIteration


if __name__ == "__main__":

# Testiamo la classe precedente:

# Il modo più semplice è quello di utilizzare il metodo for in:
    myClass = MyIterator()
    iterator = iter(myClass)  # ottengo il mio iteratore

    for i in iterator:
        print(i) # Stampa da 2 a 256...senza generare l'eccezione, cioè la gestisce internamente

    print("...l'iterazione col for in è terminata!")

    # Ricreo l'iteratore in quanto l'attributo ha il valore di 256 e facendo next otterrei l'eccezione StopIterator
    iterator = iter(myClass)  # ottengo il mio iteratore
    print(next(iterator)) #2
    print(next(iterator)) #4
    print(next(iterator)) #8
    print(next(iterator)) #16
    print(next(iterator)) #32
    print(next(iterator)) #64
    print(next(iterator))  # 128
    print(next(iterator))  # 256
    print()
    print(next(iterator))  # Ottengo l'eccezione StopIterator

    # Vediamo un esempio di un oggetto che è sia iterable che iterator....List
    myList = ["primo", "secondo", "terzo"]
    it1 = iter(myList)
    print(type(myList))  # <class 'list'>
    print()
    print(type(it1))  # <class 'list_iterator' -> cioè un iteratore di liste, un tipo particolare di iteratore
    print()
    print(next(it1))  # primo
    print(next(it1))  # secondo
    print(next(it1))  # terzo

    print(next(it1))  # Eccezione di tipo StopIteration

    # Se avessimo utilizzo il for i in MyList con una print(i) avremmo ottenuto lo stesso identico risultato

