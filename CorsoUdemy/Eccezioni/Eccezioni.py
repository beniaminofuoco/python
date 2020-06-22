# La gerarchia delle eccezioni in Python è la seguente:
# Object -> BaseException -> Exception -> ArithmeticError -> ZeroDivisionError
#
# La forma base per gestire le eccezioni ha la seguente struttura:
#   try:
#       suite
#   except:
#        suite

def div(x, y):
    return x // y

try:
    res = div(10,0)
    print(res)
except:
    print("La funzione è andata in errore!")


# Un'altra forma per la gestione dell'eccezioni prevede la possibilità
# di specificare una classe di eccezione(exception) nelle clausole except.
#   try:
#       suite
#   except exception:
#        suite
#   except exception:
#        suite

try:
    res = div(10,0)
    print(res)
except ZeroDivisionError:
    print("La funzione è andata in errore!")

# E' possibile anche gestire diversi tipi di eccezioni nella stessa clausola except
try:
    res = div(10,0)
    print(res)
except (ZeroDivisionError, ValueError):
    print("La funzione è andata in errore!")


# Il costrutto try\except può essere arricchito anche con la clausola as:
#   try:
#       suite
#   except exception as target:
#      suite
#
# la cluasola as ci consente di assegnare un nome all'eccezione e utilizzarla
# nella suite di except.
try:
    res = div(10,0)
    print(res)
except ZeroDivisionError as e:
    print(e.args)


# Oltre alle clausole precedenti è possibile usare anche le clausole: finally ed else.
# Sia finally che else sono opzionali
try:
    res = div(10,0)
    print(res)
except ZeroDivisionError as e:
    print("Errore e poi...")
finally:
    print("Finally!")

# La clusola else verrà eseguita solo se NON verranno lanciate eccezioni nel blocco try.
# IMPORTANTE: le due clausole NON sono mutualmente esclusive, ma se sono presenti entrambe
#             la clausola else deve essere posta PRIMA della cluasola finally
try:
    res = div(10,2)
except ZeroDivisionError as e:
    print("Errore e poi...")
else:
    print("Stampo il valore restituito dalla funzione: ", res)
finally:
    print("Il finally va sempre per ultimo")

# E' possibile usare la clausola raise per lanciare un'eccezione
# raise exception
# la classe di eccezione, specificata dopo la parola raise è facoltativa.
# Possiamo usare raise in diversi modi:
# raise IndexError -> specifico solo il tipo di eccezione
# raise IndexError("Errore nel loop!") -> specifico il tipo e aggiungo anche un msg di errore
for i in range(1):
    print(i)
    #raise IndexError("Errore nel loop!")

# Se non specifico nessuna classe di eccezione, la clausola raise viene usata per rilanciare
# un'eccezione che è stata generata e gestita tramite il costrutto except
try:
    res = div(10,0)
    print(res)
except ZeroDivisionError:
    print("La funzione è andata in errore!")
    #raise

# Se utilizziamo la clausola assert nel nostro programma stiamo chiedendo a Python
# di valutare un'espressione.
# Se l'expressione è vera andrà tutto bene, se è falsa viene generata un'AssertionError
# Se specifichiamo anche il parametro argument, questi verrà presentato in caso di errore
# assert expression, argument

# Genero l'errore se specifico x != 5
x= 5
assert x == 5, "Il valore è sbagliato"