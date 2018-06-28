import pika
import sys


credentials = pika.PlainCredentials('pangdahia', 'moonboss')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', type='topic')