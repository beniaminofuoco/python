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

i = 0
while True:
    message = str(i)
    i += 1
    # Andremo a consegnare il messaggio utilizzando:
    # exchange di default, cioè senza nome
    # routing_key specificheremo la coda che abbiamo definito
    # body conterrà il nostro messaggio
    channel.basic_publish(exchange='', routing_key='worker_queue', body=message)
    print("Messaggio inviato:  %s", message)
    if i > 100:
        break

connection.close()