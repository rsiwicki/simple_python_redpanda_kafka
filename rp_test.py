from confluent_kafka import Producer
import socket

conf = {'bootstrap.servers': "192.168.0.35:9092",
        'client.id': socket.gethostname()}

producer1 = Producer(conf)
topic1="my-topic-1"

producer2 = Producer(conf)
topic2="my-topic-2"

def acked1(err, msg):
    if err is not None:
        print("1 Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("1 Message produced: %s" % (str(msg)))

def acked2(err, msg):
    if err is not None:
        print("2 Failed to deliver message: %s: %s" % (str(msg), str(err)))
    else:
        print("2 Message produced: %s" % (str(msg)))

i=0
while True:
    producer1.produce(topic1, key="key", value="value", callback=acked1)
    producer2.produce(topic2, key="key", value="value", callback=acked2)

    # Wait up to 1 second for events. Callbacks will be invoked during
    # this method call if the message is acknowledged.
    producer1.poll(0)
    producer2.poll(0)

    i=i+1
    print(i)

