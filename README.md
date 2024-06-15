<h1>3 Node Kafka Cluster</h1>
<ul>
  <li> Security:
<ul>
  <li>2-way SSL handshake between Zookeeper and Kafka Brokers.</li>
  <li>SASL_SSL security protocol between all the brokers.</li>
  <li>SASL_SSL security protocol between Kafka Brokers and its external clients(producers or consumers).</li>
</li></ul>
    <li>Producer/Consumer:</li>
  <ul>
    <li>Used Confluent Python wrapper to implement Producer and Consumer applications.</li>
    <li>Implemented SASL_SSL security protocol between Kafka Brokers and Producer/Consumer.</li>
    <li>In producer, we have used the Faker library to generate new names.</li>
    <li>In producer, with security-related configurations, we have also added configurations for batching(batch.max.messages or batch.size), acks, linger.ms, queue size(queue.buffering.max.messages), etc.</li>
    <li>Below is an example showing 50 records sent from the Producer application to the Kafka Cluster and received by the Consumer application.</li>
  </ul>
</ul>

![kafka-python-output](https://github.com/Kshitij-AI/Kafka-Producer-Consumer-Python/assets/66180841/a58882a5-4bb7-4900-8547-5f8b8813993f=250x250)

