import pymongo
from pymongo import MongoClient

# Eseguo la connessione a MongoDB
client = MongoClient("localhost", 27017)

# Creo un DB e lo chiamo testdb
db = client.testdb

# Creo una collection e la chiamo persone
person_coll = db.persone

# Recupero il primo elemento della collection persone
p = person_coll.find_one()
print(p)
#{'_id': ObjectId('5ef61e32db4d40895f7cccdb'), 'nome': 'Mario', 'Cognome': 'Rossi', 'eta': 30, 'computer': ['Asus', 'Apple']}

# Recupero tutte le persone che hanno un computer Apple
res = person_coll.find({"computer":"Apple"})
for persona in res:
    print(persona)
#{'_id': ObjectId('5ef61e32db4d40895f7cccdb'), 'nome': 'Mario', 'Cognome': 'Rossi', 'eta': 30, 'computer': ['Asus', 'Apple']}
#{'_id': ObjectId('5ef61e32db4d40895f7cccdc'), 'nome': 'Giuseppe', 'Cognome': 'Verdi', 'eta': 45, 'computer': ['Apple']}

print(" **** ")

# Aggiorniamo il valore di una property all'interno di un record
update = person_coll.update_one({"nome":"Giuseppe"}, {"$set":{"eta":50}})
get = person_coll.find_one({"nome":"Giuseppe"})
print(get)

print(" **** ")

# Voglio trovare un document che ha come nome un nome > Giuseppe
findForName = person_coll.find_one({"nome" : {"$gt":"Giuseppe"}})
print(findForName)