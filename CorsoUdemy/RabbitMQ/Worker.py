import pika

print("Collegamento a RabbitMQ...")

# La prima cosa da fare è creare un oggetto Connessione per connetterci a RabbitMQ.
# Definisco i parametri che mi servono per ottenere una connessione.
# In questo caso specifico solo l'host dove gira il Server di RabbitMQ
params = pika.ConnectionParameters(host = "localhost")

# Creo la connessione
connection = pika.BlockingConnection(params)

# Richiedo un canale alla Connessione
channel =connection.channel()

# Adesso andiamo a creare una coda che sarà utilizzata dai Consumer
channel.queue_declare(queue="worker_queue")

print("...eseguito!")

def callback(chan, method, properties, body):
    print("Abbiamo ricevuto %s" %body)

# Diciamo al canale di consumare eventuali messaggi presenti nella coda worker_queue
# utilizzando la funzione callback che abbiamo definito in precedenza
# senza comunicare nessun tipo di ack (auto_ack=False)
channel.basic_consume('worker_queue', callback, auto_ack="False")

# Il Worker si mette in ascolto per consumare eventuali messaggi
channel.start_consuming()