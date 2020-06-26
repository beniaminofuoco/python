from dataclasses import dataclass

# La Data Class permettono di importare una serie di metodi all'interno di una classe che
# contiene per lo più dati. Per far cià si deve importare il decorator @dataclass
# importando il seguente import: from dataclasses import dataclass

# Il decoratore @dataclass può contenere i seguenti parametri:
# @dataclass(init=True, repr=True, order=True, frozen=False)
# questi sono i valori di default.

# Se mettiamo a False il parametro init (di default, init=True)non otteniamo nessun costruttore di default.
# Se mettiamo a False il parametro repr (di default, repr=True) non otteniamo nessuna rappresentazione "parlante"
# quando utilizziamo il metodo print.

# Il parametro order (di default, order=False) ci mette a disposizione dei metodi per utilizzare gli operatori: >, >=, <,<=
# Questi metodi confrontano le istanze di una classe confrontando i valori dei parametri
# definiti nella classe.

# Il parametro frozen (di default frozen=False) permette di "frizzare" una classe.
# Più precisamente se mettiamo frozen=True e proviamo a cambiare il valore di nome otteniamo la seguente eccezione:
# dataclasses.FrozenInstanceError: cannot assign to field 'nome'


@dataclass(order=True)
class MyClass:
    nome: str       # Questi due campi, in cui viene specificato il tipo di dato, vengono definiti:
    cognome: str    # Field e vengono utilizzati in automatico dal decorator @dataclass

    # @dataclass crea in automatico un metodo __init__ che inzializza in automatico i Field definiti
    # inoltre imprementa in automatico i metodi __repr__ (utilizzato dalla print), __eq__(==) e __ne__(!=).
    # I metodi __eq__ ed __ne__ confrontano tutti i field di una istanza per definire se due istanze
    # sono uguali o meno.

if __name__ == "__main__":
    # Il seguente costruttore ci viene fornito in automatico da @dataclass
    mc = MyClass(nome="Beniamino", cognome="Fuoco")

    # Il metodo __repr__ ci fornisce una rappresentazione più parlante
    print(mc) # MyClass(nome='Beniamino', cognome='Fuoco')
    print()

    mc2=MyClass(nome="Rossella", cognome="Preziuso")
    print(mc > mc2) # False, posso effettuare questo confronto solo se specifico il parametro order=True

