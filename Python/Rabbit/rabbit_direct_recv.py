import pika
import sys


credentials = pika.PlainCredentials('pangdahia', 'moonboss')

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue