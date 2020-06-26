import pymongo
from pymongo import MongoClient

# Eseguo la connessione a MongoDB
client = MongoClient("localhost", 27017)

# Creo un DB e lo chiamo testdb
db = client.testdb

# Creo una collection e la chiamo persone
person_coll = db.persone

# Creo degli indici sulla collection che abbiamo creato
person_coll.create_index([("nome", pymongo.ASCENDING)])
person_coll.create_index([("cognome", pymongo.ASCENDING)])
person_coll.create_index([("computer", pymongo.ASCENDING)])

# Creo un document
p1 = { "nome":"Mario", "Cognome":"Rossi", "eta":30, "computer":["Asus", "Apple"]}

# Inserisco il document all'interno della collection
person_coll.insert_one(p1)

# Creo un document
p2 = { "nome":"Giuseppe", "Cognome":"Verdi", "eta":45, "computer":["Apple"]}

# Inserisco il document all'interno della collection
person_coll.insert_one(p2)