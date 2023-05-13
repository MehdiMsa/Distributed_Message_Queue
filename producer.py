# producer.py
from confluent_kafka import Producer
import sys

# Define the Kafka configuration
conf = {'bootstrap.servers': "localhost:9092"} # Here we're pointing to HAProxy

# Create a Kafka producer
producer = Producer(conf)

# Define a callback function to handle delivery reports
def delivery_report(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Produce a message
producer.produce('my_topic', key='key', value='value', callback=delivery_report)

# Wait for any outstanding messages to be delivered and delivery reports to be received
producer.flush()

# Print producer ID
print(f'Producer {sys.argv[1]} has finished sending messages')
