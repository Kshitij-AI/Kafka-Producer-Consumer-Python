import json
import confluent_kafka as kafka

# Define JSON deserializer
def json_deserializer(msg):
    return msg.decode('utf-8')

def run_consumer():
    # Create consumer object
    consumer = kafka.Consumer(
        {
            "group.id":"demo-consumer",
            "bootstrap.servers": "localhost:9092,localhost:9093,localhost:9094",
            "security.protocol": "sasl_ssl",
            "sasl.mechanism": "SCRAM-SHA-512",
            "sasl.username": "demo-consumer",
            "sasl.password": "user1234",
            "ssl.ca.location": "D:/Kafka/kafka/sasl_ssl/ca-cert"
        }
    )

    # Subscribe to the topic from where we want to consumer data.
    consumer.subscribe(['demo-topic'])

    # Consuming messages from Kafka cluster
    try:
        while True:
            msg = consumer.poll(timeout=0.5)
            # Consumer will keep on pooling data if there is no data.
            if msg is None:
                continue
            # If there is any error while consuming message
            if msg.error():
                print(f'Error while consuming message: {msg.error()}')
                continue
            else:
                print(f'''Data consumed:
                        Topic: {msg.topic()}
                        Message: {json_deserializer(msg.value())}
                        Timestamp: {msg.timestamp()}\n''')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == "__main__":
    run_consumer()
