from itertools import combinations

inp=input("Inserisci il numero (m) fino a cui vuoi generare le combinazioni: ")
numeroMax = int(inp)
print()

pas=input("Inserisci il numero (n) della grandezza delle combinazioni: ")
passo = int(pas)

if passo > numeroMax:
    raise Exception("il numero n non può essere maggiore di m")

result =  [ x for x in combinations(range(1, numeroMax + 1), passo) ]

print(result)