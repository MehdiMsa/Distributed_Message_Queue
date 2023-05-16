# consumer.py
from confluent_kafka import Consumer, KafkaError
import sys

# Define the Kafka configuration
conf = {
    'bootstrap.servers': "localhost:9092", # Here we're pointing to HAProxy
    'group.id': f"my_group_{sys.argv[1]}", # Unique group ID for each consumer
    'auto.offset.reset': 'earliest'
}

# Create a Kafka consumer
consumer = Consumer(conf)

# Subscribe to the topic
consumer.subscribe(['my_topic'])

while True:
    # Poll for a message
    msg = consumer.poll(1.0)

    # If the message is None, continue polling
    if msg is None:
        continue

    # If there is an error, print the error and break the loop
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    # If there is no error, print the message
    print(f'Consumer {sys.argv[1]} received message: {msg.value().decode("utf-8")}')

# Close down consumer to commit final offsets
consumer.close()
