import pika
import sys
"""组播"""


credentials = pika.PlainCredentials('pangdahia', 'moonboss')

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs', exchange_type='direct')
# 严重程度(权重)