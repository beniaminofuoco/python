class ContoCorrente:

    def __init__(self, nome, conto, importo):
        self.nome = nome
        self.conto = conto
        self.__saldo = importo

    def preleva(self, importo):
        self.__saldo -= importo

    def deposita(self, importo):
        self.__saldo += importo

    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

c1 = ContoCorrente("Beniamino Fuoco", 12345, 2000)
c2 = ContoCorrente("Rossella Preziuso", 56789, 5000)

print("La situazione di partenza e' la seguente:")

c1.descrizione()
c2.descrizione()

print("")
print("Effettuo delle operazioni...")
c1.deposita(3000)
c2.preleva(1000)

print("")
c1.descrizione()
c2.descrizione()

print(c1.saldo)
c1.saldo = 1000


print("Effettuo delle operazioni...")
print("")
c1.descrizione()