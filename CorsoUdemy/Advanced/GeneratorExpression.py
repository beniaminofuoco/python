class GeneratorExpression:
    pass
# Una generator Expression è una List Compression


if __name__ == "__main__":
    numbers = [1,2,3,4,5,6,7,8,9]
    newList = [n*n for n in numbers if n % 2 ==1 ]
    print(newList) # [1, 9, 25, 49, 81]
    print(type(newList)) # <class 'list>
    # newList la possiamo scorrere quante volte vogliamo perchè è una lista
    # con una generator expression questo non è possibile

    # Generator Expression
    newGen = (n * n for n in numbers if n % 2 == 1)
    print(type(newGen)) # <class 'generator'>

    # Se proviamo a stampare il contenuto di newGen otteniamo lo stesso risultato
    for n in newGen:
        print(n)  # 1, 9, 25, 49, 81

    # Ma se ripetiamo il for non otteniamo niente
    for n in newGen:
        print(n)
    # Tutto questo accade perchè i generatori sono LAZY, cioè costruiti al momento.
    # Tutto ciò potrebbe sembrare inutile, ma quando trattiamo grandi quantità di dati è indispensabile.