#!/usr/bin/env python
import pika

#connection details
credentials = pika.PlainCredentials('arnas', 'samplepass')
parameters = pika.ConnectionParameters('localhost',
                                   5672,
                                   '/sample',
                                   credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()


#declaring queue, exchange and binding them
channel.queue_declare(queue='correct_queue', durable=True,
                   arguments={'x-message-ttl' : 3600}
                            )

channel.exchange_declare(exchange='correct_exchange', exchange_type='fanout')

channel.queue_bind(exchange='correct_exchange',
                   queue='correct_queue')

#sending the message
message = "Good day"
channel.basic_publish(
    exchange='correct_exchange',
    routing_key='',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # make message persistent
    ))

print(" [x] Sent %r" % message)
connection.close()
