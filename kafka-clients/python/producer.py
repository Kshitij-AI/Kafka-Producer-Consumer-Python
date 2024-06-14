import time
import json
import confluent_kafka as kafka
from faker import Faker  # Generate random names
from random import randint  # Generate random ids

# Funtion returns message delivery report
def delivery_report(err, msg):
    if err:
        # As we have acks as -1 with min.insync.replicas as 2.
        # This error handling is when 2/3 servers goes down.
        # It fails with KafkaError, Code: NOT_ENOUGH_REPLICAS
        if str(type(err).__name__) == "KafkaError":
            print(f"Message Delivery Failed : {str(err)}")
            print(f"Message Retry? :: {err.retriable()}")
        else:
            print(f"Message Delivery Failed: {str(err)}")
    else:
        print(
            f"Message Delivered to Partition: {msg.partition()} with Offset: {msg.offset()}"
        )
        print(f"Message: {msg.value()}")

# Define JSON serializer
def json_serializer(msg):
    return json.dumps(msg).encode('utf-8')

# Producer function
def run_producer():
    # Create producer object
    producer = kafka.Producer(
        {
            "bootstrap.servers": "localhost:9092,localhost:9093,localhost:9094",
            "security.protocol": "sasl_ssl",
            "sasl.mechanism": "SCRAM-SHA-512",
            "sasl.username": "demo-producer",
            "sasl.password": "user1234",
            "ssl.ca.location": "D:/Kafka/kafka/sasl_ssl/ca-cert",
            "acks": "-1",
            "partitioner": "consistent_random",
            'batch.num.messages':'1000',
            'linger.ms':'100',
            'queue.buffering.max.messages':'10000',
            'retries':'3'
        }
    )
    # print(producer.list_topics().brokers)
    # print(producer.list_topics().topics)

    for i in range(0, 50):
        # Generate random messages
        msg_val = {"id": randint(0, 1000), "name": Faker("en-US").name()}
        # JSON Serializer
        msg_val = json_serializer(msg_val)
        # As queue size is 10000 messages, if we try to send more than 10000 message
        # it will fail.
        # Here, we will keep trying till infinity until all the messages reach Kafka.
        # We will wait for some time till the queue gets some free space every time
        # whenever this exception occurs.
        while True:
            try:
                producer.poll(timeout=0)
                # Adding messages to queue
                producer.produce(
                    topic="demo-topic",
                    value=msg_val,
                    on_delivery=delivery_report
                )
                break
            except BufferError as buffer_error:
                print(f"{buffer_error} :: Waiting until Queue gets some free space")
                time.sleep(1)

    # Wait for all messages in the Producer queue to be delivered.
    producer.flush()


if __name__ == "__main__":
    run_producer()
