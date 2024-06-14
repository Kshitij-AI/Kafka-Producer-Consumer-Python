<h1>3 Node Kafka Cluster</h1>
<ul>
  <li> Security:
<ul>
  <li>2-way SSL handshake between Zookeeper and Kafka Brokers.</li>
  <li>SASL_SSL security protocol between all the brokers.</li>
  <li>SASL_SSL security protocol between Kafka Brokers and its external clients(producers or consumers).</li>
</li></ul>
    <li>Producer/Consumer</li>
  <ul>
    <li>Used Confluent Python wrapper to implement Producer and Consumer applications.</li>
    <li>Implemented SASL_SSL security protocol between Kafka Brokers and Producer/Consumer</li>
    <li>Below example showing 50 records sent from the Producer application to the Kafka Cluster and received by the Consumer application.</li>
    <li>https://github.com/Kshitij-AI/Kafka-Producer-Consumer-Python/assets/66180841/e0770b1d-210f-4686-8bfb-36d58c016324</li>
  </ul>
</ul>



