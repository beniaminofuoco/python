class Generator:

    @staticmethod
    def get_generator():
        e = 2
        # La parola chiave yield interrompe l'esecuzione del ciclo e ritorna il valore di e
        # subito dopo l'esecuzione riprende dalla riga successiva e continua il ciclo
        while e < 300:
            yield e
            e *= 2

    # Questa funzione è uguale alla precedente, ma utilizza return per interrompere il ciclo
    @staticmethod
    def get_generator_2():
        e = 2
        # La parola chiave yield interrompe l'esecuzione del ciclo e ritorna il valore di e
        # subito dopo l'esecuzione riprende dalla riga successiva e continua il ciclo
        while True:
            yield e
            e *= 2
            if e > 300:
                return # se richiamiamo return all'interno di un generatore viene lanciata una StopIteration

if __name__ == "__main__":
    gen = Generator.get_generator() # gen è un oggetto di tipo Generator, lo vediamo nella riga seguente:
    print(gen) #<generator object Generator.get_generator at 0x000001EF5C504120>
    print(next(gen)) # 2
    print(next(gen)) # 4
    print(next(gen)) # 8
    print(next(gen)) # 16
    print(next(gen)) # 32
    print(next(gen)) # 64
    print(next(gen)) # 128
    print(next(gen)) # 256
    print()

    # Il codice precedente è identico al seguente:
    gen = Generator.get_generator()
    print(gen.__next__())  # 2
    print(gen.__next__())  # 4
    print(gen.__next__())  # 8
    print(gen.__next__())  # 16
    print(gen.__next__())  # 32
    print(gen.__next__())  # 64
    print(gen.__next__())  # 128
    print(gen.__next__())  # 256
    print()

    print("Utilizzo il get_generator_2 -> con la return")
    gen = Generator.get_generator_2()
    for i in gen:
        print(i)