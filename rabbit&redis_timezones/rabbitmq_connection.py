import pika
from pika import exchange_type

try:    
    RABBITMQ_USER, RABBITMQ_PASS = 'johnny', '1234'

    # credentials for the connection
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASS)

    # creating connection
    connection = pika.BlockingConnection(parameters = pika.ConnectionParameters(host='localhost', credentials=credentials))

except Exception as e:
    print("Error occurred in rabbit connection: " +str(e))
    exit()

try:
    # creating channel
    channel = connection.channel()

    # creating exchange and queue
    exchange = channel.exchange_declare(exchange='exchange-1', exchange_type=exchange_type.ExchangeType.fanout)
    queue = channel.queue_declare(queue='johnny')

    # binding  exchange and queue
    channel.queue_bind(queue='johnny', exchange='exchange-1')

except Exception as e:
    print("Error occurred in rabbit configuration: " + str(e))
    exit()

def publish_message(message):
    try:
        # publishing messages to the destination
        channel.basic_publish(exchange ='exchange-1', routing_key='', body=message)
    except Exception as e:
        print("Error occurred in publish_message: " + str(e))
        exit()




