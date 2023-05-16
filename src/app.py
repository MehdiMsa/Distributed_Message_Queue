from flask import Flask, render_template, request, redirect, jsonify
from confluent_kafka import Producer, Consumer
import threading

app = Flask(__name__)

# Kafka configuration
conf = {
    'bootstrap.servers': "localhost:9092",
    'group.id': "my_group",
    'auto.offset.reset': 'earliest'
}

# Initialize producer and consumer
producer = Producer(conf)
consumer = Consumer(conf)
consumer.subscribe(['my_topic'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send', methods=['POST'])
def send_message():
    message = request.form.get('message')
    producer.produce('my_topic', key='key', value=message)
    producer.flush()
    return redirect('/')

@app.route('/receive')
def receive_message():
    msg = consumer.poll(1.0)
    if msg is None:
        return jsonify(message=None)
    else:
        return jsonify(message=msg.value().decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)
