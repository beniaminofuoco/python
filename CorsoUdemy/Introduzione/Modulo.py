# La seguente funzione prende da shell un numero e calcola se è pari o dispari
def modulo():
    # La funzione input ci permette di prendere un numero in formato Stringa dalla shell
    inp = input("Inserisci un numero: ")

    # Convertiamo inp in un intero utilizzando la funzione int
    numero = int(inp)

    # A questo punto calcoliamo il modulo 2 di numero
    modulo = numero % 2

    # Andiamo a controllare se il risultato è un numero pari o dispari
    if modulo == 0:
        print("Numero pari")
    else:
        print("Numero dispari")
